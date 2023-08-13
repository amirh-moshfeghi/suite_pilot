from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Codings'

urlpatterns = [
    path('', views.Coding_View, name='recipe_view'),
    path('chaining/', include('smart_selects.urls')),



]
