# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0020_artmmodel_treshold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artmmodel',
            name='main_modality',
        ),
    ]
