from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Child_SpecsListView.as_view(), name='Child_Specs_changelist'),
    path('add/', views.Child_SpecsCreateView.as_view(), name='Child_Specs_add'),
    path('<int:pk>/', views.Child_SpecsUpdateView.as_view(), name='Child_Specs_change'),
    path('ajax/load-values/', views.load_values, name='ajax_load_values'),
]