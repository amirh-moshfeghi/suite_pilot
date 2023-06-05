from django.contrib import admin

from Notifications.models import Notification


# Register your models here.
class NotifAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('notifications_date',)


admin.site.register(Notification, NotifAdmin)