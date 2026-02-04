from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_url, name='create-url'),
    path('edit/<int:pk>/', views.edit_url, name='edit-url'),
    path('delete/<int:pk>/', views.delete_url, name='delete-url'),
    path('<str:short_code>/', views.redirect_url, name='redirect-url'),
]
