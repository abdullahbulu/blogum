# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170401_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimda',
            name='soy_isim',
            field=models.CharField(default='sefa', max_length=32),
        ),
    ]
