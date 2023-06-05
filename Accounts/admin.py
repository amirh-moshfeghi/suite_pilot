from django.contrib import admin

from Accounts.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username',)


admin.site.register(User, UserAdmin)