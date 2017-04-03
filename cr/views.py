from django.http import HttpResponse, Http404
from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Republika
from .models import Kraje
from .models import Okresy
from .models import Mesto


class MainPageView(TemplateView):
    template_name = 'cr/index.html'


class RepublikaView(TemplateView):
    template_name = 'cr/republika.html'


class KrajeView(TemplateView):
    template_name = 'cr/kraje.html'


class OkresyView(TemplateView):
    template_name = 'cr/okresy.html'


# Json polygony
def republika_json(request):
    republika_as_geojson = serialize('geojson', Republika.objects.all())
    return HttpResponse(republika_as_geojson, content_type='json')


def kraje_json(request):
    kraje_as_geojson = serialize('geojson', Kraje.objects.all())
    return HttpResponse(kraje_as_geojson, content_type='json')


def okresy_json(request):
    okresy_as_geojson = serialize('geojson', Okresy.objects.all())
    return HttpResponse(okresy_as_geojson, content_type='json')


# Json mesta
def mesta_json(request):
    mesta_as_geojson = serialize('geojson', Mesto.objects.all())
    return HttpResponse(mesta_as_geojson, content_type='json')


def mesta_kraje_json(request):
    mesta_as_geojson = serialize('geojson', Mesto.objects.filter(krajske_mesto=True))
    return HttpResponse(mesta_as_geojson, content_type='json')


def mesta_okresy_json(request):
    mesta_as_geojson = serialize('geojson', Mesto.objects.filter(okresni_mesto=True))
    return HttpResponse(mesta_as_geojson, content_type='json')


# Detail kraj
def kraj_detail_view(request, kraj_id):
    return render(request, 'cr/kraj_detail.html', {'kraj_id': kraj_id})


def kraj_detail_json(request, kraj_id):
    try:
        kraj_gjson = serialize('geojson', Okresy.objects.filter(id_1=kraj_id))
    except:
        raise Http404("No objects with this id!")
    return HttpResponse(kraj_gjson, content_type='json')


def kraj_detail_mesta_json(request, kraj_id):
    try:
        kraj_geometry = Kraje.objects.filter(id_1=kraj_id)[0].geom
        kraj_mesta_gjson = serialize('geojson',
                                     Mesto.objects.filter(okresni_mesto=True).filter(geom__within=kraj_geometry))
    except:
        raise Http404("No objects with this id!")
    return HttpResponse(kraj_mesta_gjson, content_type='json')


# Detail okres
def okres_detail_view(request, okres_id):
    return render(request, 'cr/okres_detail.html', {'okres_id': okres_id})


def okres_detail_json(request, okres_id):
    try:
        okres_gjson = serialize('geojson', Okresy.objects.filter(id_2=okres_id))
    except:
        raise Http404("No objects with this id!")
    return HttpResponse(okres_gjson, content_type='json')


def okres_detail_mesta_json(request, okres_id):
    try:
        okres_geometry = Okresy.objects.filter(id_2=okres_id)[0].geom
        okres_mesta_gjson = serialize('geojson', Mesto.objects.filter(geom__within=okres_geometry))
    except:
        raise Http404("No objects with this id!")
    return HttpResponse(okres_mesta_gjson, content_type='json')
