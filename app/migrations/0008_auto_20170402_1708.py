# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170402_1623'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programs',
            new_name='Home',
        ),
        migrations.RenameModel(
            old_name='Postblog',
            new_name='Program',
        ),
        migrations.RenameModel(
            old_name='Technologies',
            new_name='Technology',
        ),
    ]