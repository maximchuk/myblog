# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160401_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 21, 9, 23, 705545), verbose_name='Дата изминения'),
        ),
    ]
