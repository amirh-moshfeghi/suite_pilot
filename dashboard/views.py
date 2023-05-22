from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "dashboard/index.html")

def projects(request):
    return render(request, "dashboards/projects.html")

def test(request):
    return render(request, "dashboard/index2.html")

def home(request):
    return render(request, "dashboard/home.html")