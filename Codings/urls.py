from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Codings'

urlpatterns = [
    path('', views.recipe_view.as_view(), name='home'),
    path('chaining/', include('smart_selects.urls')),



]
