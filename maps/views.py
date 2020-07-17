from django.shortcuts import render
import datetime as dt
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Maps
from django.contrib.gis.geos import Point

# GeoJSONLayerView

longitude = 36.7753212
latitude = -1.2559551
nodes = 6164144598

user_location = Point(longitude , latitude, srid=4326)

# Create your views here.
class Home(generic.ListView):
    date = dt.date.today()
    model = Maps
    context_object_name = 'maps'
    queryset = Maps.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'index.html'

