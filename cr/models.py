from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Republika(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_engli = models.CharField(max_length=50)
    name_iso = models.CharField(max_length=54)
    name_fao = models.CharField(max_length=50)
    name_local = models.CharField(max_length=54)
    name_obsol = models.CharField(max_length=150)
    name_varia = models.CharField(max_length=160)
    name_nonla = models.CharField(max_length=50)
    name_frenc = models.CharField(max_length=50)
    name_spani = models.CharField(max_length=50)
    name_russi = models.CharField(max_length=50)
    name_arabi = models.CharField(max_length=50)
    name_chine = models.CharField(max_length=50)
    waspartof = models.CharField(max_length=100)
    contains = models.CharField(max_length=50)
    sovereign = models.CharField(max_length=40)
    iso2 = models.CharField(max_length=4)
    www = models.CharField(max_length=2)
    fips = models.CharField(max_length=6)
    ison = models.FloatField()
    validfr = models.CharField(max_length=12)
    validto = models.CharField(max_length=10)
    pop2000 = models.FloatField()
    sqkm = models.FloatField()
    popsqkm = models.FloatField()
    unregion1 = models.CharField(max_length=254)
    unregion2 = models.CharField(max_length=254)
    developing = models.FloatField()
    cis = models.FloatField()
    transition = models.FloatField()
    oecd = models.FloatField()
    wbregion = models.CharField(max_length=254)
    wbincome = models.CharField(max_length=254)
    wbdebt = models.CharField(max_length=254)
    wbother = models.CharField(max_length=254)
    ceeac = models.FloatField()
    cemac = models.FloatField()
    ceplg = models.FloatField()
    comesa = models.FloatField()
    eac = models.FloatField()
    ecowas = models.FloatField()
    igad = models.FloatField()
    ioc = models.FloatField()
    mru = models.FloatField()
    sacu = models.FloatField()
    uemoa = models.FloatField()
    uma = models.FloatField()
    palop = models.FloatField()
    parta = models.FloatField()
    cacm = models.FloatField()
    eurasec = models.FloatField()
    agadir = models.FloatField()
    saarc = models.FloatField()
    asean = models.FloatField()
    nafta = models.FloatField()
    gcc = models.FloatField()
    csn = models.FloatField()
    caricom = models.FloatField()
    eu = models.FloatField()
    can = models.FloatField()
    acp = models.FloatField()
    landlocked = models.FloatField()
    aosis = models.FloatField()
    sids = models.FloatField()
    islands = models.FloatField()
    ldc = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '{}'.format(self.name_engli)

    def __unicode__(self):
        return '{}'.format(self.name_engli)


class Mesto(models.Model):
    obec = models.CharField(max_length=50)
    kod_obce = models.IntegerField(blank=True, null=True)
    okres = models.CharField(max_length=20, blank=True, null=True)
    kod_okresu = models.CharField(max_length=6, blank=True, null=True)
    kraj = models.CharField(max_length=20, blank=True, null=True)
    kod_kraje = models.CharField(max_length=5, blank=True, null=True)
    psc = models.IntegerField(blank=True, null=True)
    geom = models.PointField('lon/lat', blank=True, null=True)
    okresni_mesto = models.BooleanField(default=False)
    krajske_mesto = models.BooleanField(default=False)
    objects = models.GeoManager()

    def __str__(self):
        return '{}'.format(self.obec)

    def __unicode__(self):
        return '{}'.format(self.obec)


class Kraje(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    hasc_1 = models.CharField(max_length=15)
    ccn_1 = models.IntegerField()
    cca_1 = models.CharField(max_length=254)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    nl_name_1 = models.CharField(max_length=50)
    varname_1 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '{}'.format(self.name_1)

    def __unicode__(self):
        return '{}'.format(self.name_1)


class Okresy(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=75)
    hasc_2 = models.CharField(max_length=15)
    ccn_2 = models.IntegerField()
    cca_2 = models.CharField(max_length=254)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    nl_name_2 = models.CharField(max_length=75)
    varname_2 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return '{}'.format(self.name_2)

    def __unicode__(self):
        return '{}'.format(self.name_2)
