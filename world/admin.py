from django.contrib.gis import admin
from .models import WorldBorder, Profile


# Register your models here.

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Profile, admin.OSMGeoAdmin)