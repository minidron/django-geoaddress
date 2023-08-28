# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_geoaddress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseaddress',
            name='apartment',
            field=models.CharField(max_length=30, verbose_name='\u043e\u0444\u0438\u0441', blank=True),
        ),
    ]
