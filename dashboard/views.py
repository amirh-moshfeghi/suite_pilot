from django.shortcuts import render

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

def create_hr_final(request):
    return render(request, "dashboard/create_hr_final.html")