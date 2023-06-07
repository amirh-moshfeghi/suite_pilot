from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from HR.models import Manager, Level, Company, Position, OU, Department


# Register your models here.
class ManagerAdmin(admin.ModelAdmin):

    search_fields = ('persian_name',)

class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Department)
admin.site.register(OU)
admin.site.register(Position)
admin.site.register(Company,textEditorAdmin)
admin.site.register(Level)