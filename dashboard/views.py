from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
import csv
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, "dashboard/index_final.html")


