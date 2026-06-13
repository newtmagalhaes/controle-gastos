"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Base
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # Libs
    # Apps
    path('gastos/', include('apps.core.urls')),
    path('', RedirectView.as_view(url='gastos')),
]
