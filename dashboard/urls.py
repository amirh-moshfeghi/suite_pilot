from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('wm_create/', views.wm_create, name='wm_create'),
    path('wm_create2/', views.wm_create_2, name='wm_create_2'),
    path('hr_create/', views.hr_create, name='hr_create'),
    path('home/', views.home, name='home'),
    path('index/', views.index_2, name='index'),
    path('index_final/', views.index_final, name='index_final'),
    path('create_hr_final/', views.create_hr_manager, name='create_hr_manager'),

]
