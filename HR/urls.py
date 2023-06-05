from django.urls import path
from . import views
from .views import export_managers_csv

urlpatterns = [
    path('Base_information_Manager/', views.Base_information_Manager, name='Base_information_Manager'),
    path('Company/Base_Information', views.Company_Base_Information, name='Company_Base_Information'),
    path('Department/Base_Information', views.Department_Base_Information, name='Department_Base_Information'),
    path('OU/Base_Information', views.OU_Base_Information, name='OU_Base_Information'),
    path('export/', export_managers_csv, name='export_managers_csv'),
    path('Company/Base_Information/Update_Company/<int:id>', views.Update_Company, name='Update_Company'),
    path('Department/Base_Information/Update_Department/<int:id>', views.Update_Department, name='Update_Department'),
    path('OU/Base_Information/Update_OU/<int:id>', views.Update_OU, name='Update_OU'),
    path('Base_information_Manager/update_manager/<int:id>', views.update_manager, name='update_manager'),
    path('Base_information_Manager/delete_manager/<int:id>', views.delete_manager, name='delete_manager'),
    path('Base_information_Manager/update_manager/update_manager_record/<int:id>', views.update_manager_record, name='update_manager_record'),
    path('Company/Base_Information/Update_Company/Update_Company_Record/<int:id>', views.Update_Company_Base_Information, name='Update_Company_Base_Information'),
    path('Department/Base_Information/Update_Company/Update_Department_Record/<int:id>', views.Update_Department_Base_Information, name='Update_Department_Base_Information'),
    path('OU/Base_Information/Update_OU/Update_OU_Record/<int:id>', views.Update_OU_Base_Information, name='Update_OU_Base_Information'),

]
