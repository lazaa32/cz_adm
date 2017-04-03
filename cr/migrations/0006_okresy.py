# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 17:01
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0005_kraje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okresy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_0', models.IntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.IntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('id_2', models.IntegerField()),
                ('name_2', models.CharField(max_length=75)),
                ('hasc_2', models.CharField(max_length=15)),
                ('ccn_2', models.IntegerField()),
                ('cca_2', models.CharField(max_length=254)),
                ('type_2', models.CharField(max_length=50)),
                ('engtype_2', models.CharField(max_length=50)),
                ('nl_name_2', models.CharField(max_length=75)),
                ('varname_2', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]