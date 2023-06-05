from django.contrib import admin

from HR.models import Manager, Level, Company, Position, OU, Department


# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    search_fields = ('persian_name',)


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Department)
admin.site.register(OU)
admin.site.register(Position)
admin.site.register(Company)
admin.site.register(Level)