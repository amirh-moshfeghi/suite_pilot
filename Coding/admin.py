from django.contrib import admin

from Coding.models import MaterialGroup, IdentityGroup, Child, Values, SP

# Register your models here.
admin.site.register(MaterialGroup)
admin.site.register(IdentityGroup)
admin.site.register(Child)
admin.site.register(Values)
admin.site.register(SP)