from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "dashboard/index.html")

def projects(request):
    return render(request, "dashboards/projects.html")