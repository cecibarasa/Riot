from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Riot

# Register your models here.
@admin.register(Riot)
class RiotAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')