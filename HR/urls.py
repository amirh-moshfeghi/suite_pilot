from django.urls import path
from . import views
from .views import export_managers_csv

urlpatterns = [
    path('Base_information_Manager/', views.Base_information_Manager, name='Base_information_Manager'),
    path('export/', export_managers_csv, name='export_managers_csv'),
    path('Base_information_Manager/update_manager/<int:id>', views.update_manager, name='update_manager'),
    path('Base_information/delete_manager/<int:id>', views.delete_manager, name='delete_manager'),
    path('Base_information_Manager/update_manager/update_manager_record/<int:id>', views.update_manager_record, name='update_manager_record'),

]
