from django.contrib import gis
from django.contrib import admin
from .models import Republika
from .models import Mesto
from .models import Kraje
from .models import Okresy


class FilterAdmin(admin.ModelAdmin):
    list_display = ('obec', 'krajske_mesto', 'okresni_mesto')
    search_fields = ['obec']

admin.site.register(Republika, gis.admin.OSMGeoAdmin)
admin.site.register(Mesto, FilterAdmin)
admin.site.register(Kraje, gis.admin.OSMGeoAdmin)
admin.site.register(Okresy, gis.admin.OSMGeoAdmin)
