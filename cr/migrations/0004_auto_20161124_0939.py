# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 09:39
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0003_auto_20161124_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesto',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='lon/lat'),
        ),
    ]