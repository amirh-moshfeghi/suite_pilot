from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/delete/<int:id>/', views.delete, name='delete_task'),
    path('notes/complete/<int:id>/', views.complete, name='completed_task'),
    path('notes/', views.tasks, name='tasks'),
    path('test/', views.test, name='test'),
]