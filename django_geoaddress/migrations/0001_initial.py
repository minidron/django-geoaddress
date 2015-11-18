# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=255, verbose_name='\u043e\u0431\u043b\u0430\u0441\u0442\u044c', blank=True)),
                ('subarea', models.CharField(max_length=255, verbose_name='\u0440\u0430\u0439\u043e\u043d', blank=True)),
                ('locality', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0441\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u043f\u0443\u043d\u043a\u0442')),
                ('street', models.CharField(max_length=255, verbose_name='\u0443\u043b\u0438\u0446\u0430', blank=True)),
                ('house', models.CharField(max_length=50, verbose_name='\u0434\u043e\u043c', blank=True)),
                ('apartment', models.CharField(max_length=10, verbose_name='\u043e\u0444\u0438\u0441', blank=True)),
                ('zip', models.CharField(max_length=10, verbose_name='\u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441', blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='\u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b', blank=True)),
            ],
            options={
                'verbose_name': '\u0430\u0434\u0440\u0435\u0441',
                'verbose_name_plural': '\u0430\u0434\u0440\u0435\u0441\u0430',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0430',
                'verbose_name_plural': '\u0441\u0442\u0440\u0430\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('coordinates', django.contrib.gis.db.models.fields.PolygonField(srid=4326, verbose_name='\u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0440\u0435\u0433\u0438\u043e\u043d',
                'verbose_name_plural': '\u0440\u0435\u0433\u0438\u043e\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='baseaddress',
            name='country',
            field=models.ForeignKey(verbose_name='\u0441\u0442\u0440\u0430\u043d\u0430', to='django_geoaddress.Country'),
        ),
    ]
