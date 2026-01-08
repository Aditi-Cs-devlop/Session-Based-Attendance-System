"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # for redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('session/', include('attendance_sessions.urls')),
    # Redirect base URL '/' to session control page
    path('', RedirectView.as_view(url='/session/control/', permanent=False)),
]