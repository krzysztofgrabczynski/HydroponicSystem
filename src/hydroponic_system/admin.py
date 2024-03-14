from django.contrib import admin

from src.hydroponic_system.models import HydroponicSystem, Measurement

admin.site.register(HydroponicSystem)
admin.site.register(Measurement)
