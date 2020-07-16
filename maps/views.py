from django.shortcuts import render
import datetime as dt
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Riot
from django.contrib.gis.geos.point import Point


longitude = 36.8278143
latitude = -1.314117

user_location = Point(longitude, latitude, srid=4326)

# Create your views here.
# def home(request):
#     date = dt.date.today()
#     return render(request, 'index.html', {"date": date})

class Home(generic.ListView):
    model = Riot
    context_object_name = 'maps'
    queryset = Riot.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:1200]
    template_name = 'index.html'