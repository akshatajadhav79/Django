from django.contrib import admin
from staff.models import staffMaster, staffTypesMaster ,MenuMaster

# Register your models here.

admin.site.register(staffMaster)
admin.site.register(staffTypesMaster)

admin.site.register(MenuMaster)