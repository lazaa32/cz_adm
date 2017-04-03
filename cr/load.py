import os
from django.contrib.gis import geos
from django.contrib.gis.utils import LayerMapping
from .models import Republika
from .models import Mesto
from .models import Kraje
from .models import Okresy

# Auto-generated `LayerMapping` dictionary for Republika model
republika_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_engli' : 'NAME_ENGLI',
    'name_iso' : 'NAME_ISO',
    'name_fao' : 'NAME_FAO',
    'name_local' : 'NAME_LOCAL',
    'name_obsol' : 'NAME_OBSOL',
    'name_varia' : 'NAME_VARIA',
    'name_nonla' : 'NAME_NONLA',
    'name_frenc' : 'NAME_FRENC',
    'name_spani' : 'NAME_SPANI',
    'name_russi' : 'NAME_RUSSI',
    'name_arabi' : 'NAME_ARABI',
    'name_chine' : 'NAME_CHINE',
    'waspartof' : 'WASPARTOF',
    'contains' : 'CONTAINS',
    'sovereign' : 'SOVEREIGN',
    'iso2' : 'ISO2',
    'www' : 'WWW',
    'fips' : 'FIPS',
    'ison' : 'ISON',
    'validfr' : 'VALIDFR',
    'validto' : 'VALIDTO',
    'pop2000' : 'POP2000',
    'sqkm' : 'SQKM',
    'popsqkm' : 'POPSQKM',
    'unregion1' : 'UNREGION1',
    'unregion2' : 'UNREGION2',
    'developing' : 'DEVELOPING',
    'cis' : 'CIS',
    'transition' : 'Transition',
    'oecd' : 'OECD',
    'wbregion' : 'WBREGION',
    'wbincome' : 'WBINCOME',
    'wbdebt' : 'WBDEBT',
    'wbother' : 'WBOTHER',
    'ceeac' : 'CEEAC',
    'cemac' : 'CEMAC',
    'ceplg' : 'CEPLG',
    'comesa' : 'COMESA',
    'eac' : 'EAC',
    'ecowas' : 'ECOWAS',
    'igad' : 'IGAD',
    'ioc' : 'IOC',
    'mru' : 'MRU',
    'sacu' : 'SACU',
    'uemoa' : 'UEMOA',
    'uma' : 'UMA',
    'palop' : 'PALOP',
    'parta' : 'PARTA',
    'cacm' : 'CACM',
    'eurasec' : 'EurAsEC',
    'agadir' : 'Agadir',
    'saarc' : 'SAARC',
    'asean' : 'ASEAN',
    'nafta' : 'NAFTA',
    'gcc' : 'GCC',
    'csn' : 'CSN',
    'caricom' : 'CARICOM',
    'eu' : 'EU',
    'can' : 'CAN',
    'acp' : 'ACP',
    'landlocked' : 'Landlocked',
    'aosis' : 'AOSIS',
    'sids' : 'SIDS',
    'islands' : 'Islands',
    'ldc' : 'LDC',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Kraje model
kraje_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'hasc_1' : 'HASC_1',
    'ccn_1' : 'CCN_1',
    'cca_1' : 'CCA_1',
    'type_1' : 'TYPE_1',
    'engtype_1' : 'ENGTYPE_1',
    'nl_name_1' : 'NL_NAME_1',
    'varname_1' : 'VARNAME_1',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Okresy model
okresy_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_0' : 'NAME_0',
    'id_1' : 'ID_1',
    'name_1' : 'NAME_1',
    'id_2' : 'ID_2',
    'name_2' : 'NAME_2',
    'hasc_2' : 'HASC_2',
    'ccn_2' : 'CCN_2',
    'cca_2' : 'CCA_2',
    'type_2' : 'TYPE_2',
    'engtype_2' : 'ENGTYPE_2',
    'nl_name_2' : 'NL_NAME_2',
    'varname_2' : 'VARNAME_2',
    'geom' : 'MULTIPOLYGON',
}


# Data source
republika_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'CZE_adm0.shp'))
kraje_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'CZE_adm1.shp'))
okresy_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'CZE_adm2.shp'))
mesta_lite_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'mesta_lite.csv'))
mesta_kraje_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'mesta_kraje.csv'))
mesta_all_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'mesta_all.csv'))


def republika_load(verbose=True):
    lm = LayerMapping(Republika, republika_shp, republika_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)


def kraje_load(verbose=True):
    lm2 = LayerMapping(Kraje, kraje_shp, kraje_mapping, transform=False, encoding='utf-8')
    lm2.save(strict=True, verbose=verbose)


def okresy_load(verbose=True):
    lm3 = LayerMapping(Okresy, okresy_shp, okresy_mapping, transform=False, encoding='utf-8')
    lm3.save(strict=True, verbose=verbose)


def mesta_kraje_load():
    with open(mesta_kraje_csv) as point_file:
        for line in point_file:
            obec, kod_obce, okres, kod_okresu, kraj, kod_kraje, psc, lat, lon = line.split(',')
            point = "POINT({} {})".format(lon.strip(), lat.strip())
            Mesto.objects.create(obec=obec, kod_obce=kod_obce, okres=okres, kod_okresu=kod_okresu,
                                 kraj=kraj, kod_kraje=kod_kraje, psc=psc, geom=geos.fromstr(point))


def mesta_load():
    with open(mesta_all_csv) as point_file:
        for line in point_file:
            obec, kod_obce, okres, kod_okresu, kraj, kod_kraje, psc, lat, lon = line.split(',')
            point = "POINT({} {})".format(lon.strip(), lat.strip())
            Mesto.objects.create(obec=obec, kod_obce=kod_obce, okres=okres, kod_okresu=kod_okresu,
                                 kraj=kraj, kod_kraje=kod_kraje, psc=psc, geom=geos.fromstr(point),
                                 okresni_mesto=(obec == okres), krajske_mesto=(obec == kraj))


def run(verbose=True):
    republika_load(verbose=verbose)
    kraje_load(verbose=verbose)
    okresy_load(verbose=verbose)
    mesta_load()
