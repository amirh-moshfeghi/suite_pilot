from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "dashboard/index.html")

def projects(request):
    return render(request, "dashboards/projects.html")

def wm_create(request):
    return render(request, "dashboard/wm_create.html")

def home(request):
    return render(request, "dashboard/home.html")