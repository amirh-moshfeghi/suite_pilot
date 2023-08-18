from django.db.models import Q, F
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from Accounts.models import AuditEntry
from Coding.models import MaterialGroup, Child
from dashboard.models import QuickLinks, SubMenu

IDENTITY = None
CHILD = None


def coding_view(request):
    material_group_qs = MaterialGroup.objects.all()
    current_user_username=request.user.username
    current_user_logs = AuditEntry.objects.filter(username=current_user_username)
    quick_links = QuickLinks.objects.all()
    submenu = SubMenu.objects.all()
    return render(request, 'Coding/Coding_New_Style.html', {'material_group_qs':material_group_qs,'current_user_logs':current_user_logs,'quick_links':quick_links,'submenu':submenu})


def json_material_group_data(request):
    material_qs_val = list(MaterialGroup.objects.values())
    return JsonResponse({'data':material_qs_val})


def json_material_group_parent_data(request,*args, **kwargs):
    obj_parent = list(MaterialGroup.objects.filter(is_parent='True').values())
    return JsonResponse({'data': obj_parent})


def json_material_group_selected_data(request,*args, **kwargs):
    selected_material_group = kwargs.get('material_group')
    # material_list = MaterialGroup.objects.filter(i__contains=selected_material_group)
    # print(material_list, 'material_list')
    obj_parent_list = (MaterialGroup.objects.filter(material_group=selected_material_group).values('material_parent_id'))
    # obj_identity_group = list(MaterialGroup.objects.values('identity_reference'))
    first_value = list(obj_parent_list.first().items())[0][1]
    obj_identity_group = list(MaterialGroup.objects.filter(material_parent_id=first_value).values())


    # print(obj_identity_group)
    return JsonResponse({'data': obj_identity_group})


def json_identity_group_selected_data(request,*args, **kwargs):
    selected_identity = kwargs.get('identity_group')
    obj_child_group = list(Child.objects.filter(material_group__material_group=selected_identity).values())
    print(obj_child_group)
    obj_child_desc = list(Child.objects.filter(material_group__material_group=selected_identity).values('child_desc'))[0]['child_desc']
    # obj_child_group = list(Child.objects.filter(material_group__material_group=selected_identity).values_list()[0])
    # same_objs = list(
    #     Child.objects.filter(child_group_id__exact=F('child_group__child_value_id')).values('value_desc'))
    # same_objs = \
    # list(Child.objects.filter(child_parent_id__exact=F('material_group__parent_child_id')).values_list('child_desc'))[0]
    # a=[]
    # for dic in obj_child_desc:
    #     for val, cal in dic.items():
    #         a.append(cal)
            # print(f'{val} is {cal}')
    print(obj_child_desc)


    return JsonResponse({'data':  obj_child_group})


# def json_child_group_data(request,*args, **kwargs):
#     # selected_identity = kwargs.get('material_group')
#     # obj_child_group = list(Child.objects.filter(material_group__material_group=selected_identity).values('child_group'))
#     # print(obj_child_group,'obj')
#
#     # obj_value_group = list(Values.objects.values_list('value','child_id_as_child'))
#     # obj_child_group = list(Values.objects.values_list('child_group_id').values('value_desc'))
#     # value_obj_group = (Values.objects.values_list('child_id_as_child').values())
#     # child_obj_group = (Child.objects.values_list('child_id_as_parent').values())
#     # obj_child_group = list(Child.objects.values_list('child_id_as_parent'))
#     # intersects = Child.objects.filter(child_id_as_parent=Values.objects.values_list('child_id_as_child'))
#
#
#
#     # obj_child_group = list(Values.objects.filter(child_group__child_group=GLOBAL_Entry).values('value'))
#
#     # print(Values.objects.select_related().filter(child_id_as_child=1))
#     # print(Values.objects.select_related('child_id_as_parent').filter(child_id_as_parent=child))
#
#     print(same_objs)
#
#     return JsonResponse({'data': same_objs})
