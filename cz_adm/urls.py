"""cz_adm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib.gis import admin
from cr.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPageView.as_view()),

    # GJSON
    # Polygons - data
    url(r'^republika.data/', republika_json, name='republika'),
    url(r'^kraje.data/', kraje_json, name='kraje'),
    url(r'^okresy.data/', okresy_json, name='okresy'),
    # Points - data
    url(r'^mesta.data/', mesta_json, name='mesta'),
    url(r'^kraje_mesta.data/', mesta_kraje_json, name='kraje_mesta'),
    url(r'^okresy_mesta.data/', mesta_okresy_json, name='okresy_mesta'),

    # Kraj detail
    url(r'^kraj.data/(?P<kraj_id>\d+)/', kraj_detail_json, name='kraj_detail'),
    url(r'^kraj_mesta.data/(?P<kraj_id>\d+)/', kraj_detail_mesta_json, name='kraj_detail_mesta'),
    url(r'^kraj/(?P<kraj_id>\d+)', kraj_detail_view),

    # Okres detail
    url(r'^okres.data/(?P<okres_id>\d+)/', okres_detail_json, name='okres_detail'),
    url(r'^okres_mesta.data/(?P<okres_id>\d+)/', okres_detail_mesta_json, name='okres_detail_mesta'),
    url(r'^okres/(?P<okres_id>\d+)', okres_detail_view),


    # General
    url(r'^republika/', RepublikaView.as_view()),
    url(r'^kraje/', KrajeView.as_view()),
    url(r'^okresy/', OkresyView.as_view()),
]
