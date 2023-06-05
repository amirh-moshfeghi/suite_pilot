from django.contrib import admin
from Accounts.models import AuditEntry
from Accounts.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username',)


class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip', 'time',]
    list_filter = ['action',]
    readonly_fields = ('time',)


admin.site.register(User, UserAdmin)
admin.site.register(AuditEntry, AuditEntryAdmin)




