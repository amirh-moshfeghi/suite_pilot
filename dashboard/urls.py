from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    
]
