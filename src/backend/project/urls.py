"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('manager/', include('apps.manager.urls')),
    path('gastos/', include('apps.core.urls')),
    path('', RedirectView.as_view(url='gastos')),
]
