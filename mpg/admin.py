from django.contrib import admin

from .models import MpgUser, Make, Model, Vehicle, FuelUp

# Register your models here.
admin.site.register(MpgUser)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Vehicle)
admin.site.register(FuelUp)


