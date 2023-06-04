from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
import csv
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from Notifications.models import Notification
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required



@login_required()
def home(request):
    return render(request, "dashboard/index_final.html")

@login_required()
def notifs_box(request):
    context = {
        "page_title": "پیام ها",
        "notifs": Notification.objects.all().order_by('-publish')
    }
    return render(request, "dashboard/index_final.html", context)