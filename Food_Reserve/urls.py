from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Food_Reserve'

urlpatterns = [
    path('food_reserve/', views.Food_Reserve_Base_Information, name='Food_Reserve_Base_Information'),

]
