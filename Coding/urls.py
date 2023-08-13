from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.coding_view, name='coding_view'),
    path('Material_Group_All/', views.json_material_group_data, name='Material_Group'),
    path('Material_Group_Selected/<str:material_group>/', views.json_material_group_selected_data, name='Material_Group_Selected'),
    path('Identity_Group_Selected/<str:material_group>/<str:identity_group>', views.json_identity_group_selected_data, name='Identity_Group_Selected'),
    path('Identity_Group_Selected/<str:material_group>/<str:identity_group>/<str:child_group>', views.json_child_group_data, name='Child_Group_Selected'),

]