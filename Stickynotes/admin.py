from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from Stickynotes.models import Guest, Business, Booking

admin.site.register(Guest)
admin.site.register(Business)
admin.site.register(Booking)
