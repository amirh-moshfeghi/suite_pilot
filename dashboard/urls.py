from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('wm_create/', views.wm_create, name='wm_create'),
    path('home/', views.home, name='home'),
    
]
