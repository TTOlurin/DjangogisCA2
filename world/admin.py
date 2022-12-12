from django.contrib.gis import admin
from .models import WorldBorder, Profile
from django.contrib.gis.admin import OSMGeoAdmin


# Register your models here.

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Profile, admin.OSMGeoAdmin)

# @admin.register(Restaurants)
# class RestaurantsAdmin(OSMGeoAdmin):
#     list_display = ('name', 'address', 'location')