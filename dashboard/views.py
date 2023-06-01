from django.shortcuts import render
from .forms import ManagerForm
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
import sweetify
# Create your views here.


def home(request):
    return render(request, "dashboard/index.html")

def projects(request):
    return render(request, "dashboards/projects.html")

def wm_create(request):
    return render(request, "dashboard/wm_create.html")

def hr_create(request):
    return render(request, "dashboard/hr_create.html")

def index_2(request):
    return render(request, "dashboard/index3.html")

def wm_create_2(request):
    return render(request, "dashboard/wm_create_2.html")

def home(request):
    return render(request, "dashboard/home.html")

def index_final(request):
    return render(request, "dashboard/index_final.html")

def create_hr_manager(request):
    if request.method == "POST":
        manager_form = ManagerForm(request.POST, request.FILES)
        if manager_form.is_valid():
            manager_form.save()
            messages.success(request,'ثبت مدیر با موفقیت انجام شد')
        else:
            messages.error(request, 'مشکلی در ورودی اطلاعات.لطفا مجدد تلاش کنید')

        return redirect("create_hr_manager")
    manager_form = ManagerForm()
    managers = Manager.objects.all()
    return render(request=request, template_name="dashboard/create_hr_final.html", context={'manager_form': manager_form, 'managers': managers})