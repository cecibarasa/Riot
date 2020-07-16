from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Maps

@admin.register(Maps)
class MapsAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
# Register your models here.
