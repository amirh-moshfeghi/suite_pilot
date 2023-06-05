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
from Accounts.models import AuditEntry
from django.contrib.gis.geoip2 import GeoIP2





@login_required()
def home(request):
    current_user_username=request.user.username
    current_user_logs = AuditEntry.objects.filter(username=current_user_username)

    # g = GeoIP2()

    print(current_user_logs[0].ip)
    return render(request, "dashboard/index_final.html",{'current_user_logs':current_user_logs})

@login_required()
def notifs_box(request):
    context = {
        "page_title": "پیام ها",
        "notifs": Notification.objects.all().order_by('-publish')
    }
    return render(request, "dashboard/index_final.html", context)