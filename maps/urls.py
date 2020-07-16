from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.urls import path
from maps import views
from django.views.generic import TemplateView
from .models import Maps
from djgeojson.views import GeoJSONLayerView


urlpatterns=[
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^data/$', GeoJSONLayerView.as_view(model=Maps, properties=("name","location","address","city")), name="data")
]