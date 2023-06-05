from django.contrib import admin

from Forms.form import PostAdminForm
from Forms.models import FormLetters


# Register your models here.
class FormsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    form = PostAdminForm


admin.site.register(FormLetters, FormsAdmin)