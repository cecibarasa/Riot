from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView
from .models import Riot
from djgeojson.views import GeoJSONLayerView

urlpatterns=[
    # url('^$',views.home,name='home'),
    path('', views.Home.as_view()),
    url(r'ˆ$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'ˆdata/$', GeoJSONLayerView.as_view(model=Riot), name='data'),

    
]