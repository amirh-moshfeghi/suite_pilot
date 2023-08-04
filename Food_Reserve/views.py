from django.contrib import messages
from django.shortcuts import render, redirect

from dashboard.models import SubMenu, QuickLinks


# Create your views here.
def Food_Reserve_Base_Information(request):

    quick_links = QuickLinks.objects.all()
    submenu = SubMenu.objects.all()
    return render(request=request, template_name="Food_Reserve/Food_Reserve_New_Style.html", context={'quick_links':quick_links,'submenu':submenu})
