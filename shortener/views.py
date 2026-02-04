from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import ShortURL
from .forms import ShortURLForm
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def redirect_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)

    if url.is_expired():
        return HttpResponse("This link has expired")

    url.click_count += 1
    url.save()
    return redirect(url.original_url)

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shortener/dashboard.html', {'urls': urls})

@login_required
def create_url(request):
    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.user = request.user
            custom_code = form.cleaned_data.get('custom_code')
            if custom_code:
                short_url.short_code = custom_code
            short_url.save()
            return redirect('dashboard')
    else:
        form = ShortURLForm()
    return render(request, 'shortener/create_edit_url.html', {'form': form})

@login_required
def edit_url(request, pk):
    short_url = get_object_or_404(ShortURL, pk=pk, user=request.user)
    if request.method == "POST":
        form = ShortURLForm(request.POST, instance=short_url)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ShortURLForm(instance=short_url)
    return render(request, 'shortener/create_edit_url.html', {'form': form})

@login_required
def delete_url(request, pk):
    short_url = get_object_or_404(ShortURL, pk=pk, user=request.user)
    if request.method == "POST":
        short_url.delete()
        return redirect('dashboard')
    return render(request, 'shortener/delete_url.html', {'short_url': short_url})
