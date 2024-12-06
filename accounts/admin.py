from django.contrib import admin
from accounts.models import BookingMaster,contactMaster,AdvatureMaster,ServiceMaster, User

# Register your models here.


# admin.site.register(Profile)
admin.site.register(BookingMaster)
admin.site.register(contactMaster)
admin.site.register(AdvatureMaster)
admin.site.register(ServiceMaster)
