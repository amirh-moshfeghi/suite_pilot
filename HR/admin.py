from django.contrib import admin

from HR.models import Manager


# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    search_fields = ('persian_name',)


admin.site.register(Manager, ManagerAdmin)