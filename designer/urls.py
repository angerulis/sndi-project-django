from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('creermodele/', views.buildmodele, name='modeleForm'),
    path('preview/', views.preview, name='previewLayout'),
]
