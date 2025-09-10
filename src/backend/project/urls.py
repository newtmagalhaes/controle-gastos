"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.urls import include, path

urlpatterns = [
    path('manager/', include('apps.manager.urls')),
]
