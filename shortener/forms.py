from django import forms
from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    custom_code = forms.CharField(
        max_length=10, required=False, help_text="Optional custom short code"
    )

    class Meta:
        model = ShortURL
        fields = ['original_url', 'expires_at']

    def clean_custom_code(self):
        code = self.cleaned_data.get('custom_code')
        if code:
            if ShortURL.objects.filter(short_code=code).exists():
                raise forms.ValidationError("This code is already in use.")
            if not code.isalnum():
                raise forms.ValidationError("Only letters and numbers are allowed.")
        return code
