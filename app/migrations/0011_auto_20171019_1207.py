# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170402_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='soy_isim',
            field=models.CharField(default='', max_length=32),
        ),
    ]
