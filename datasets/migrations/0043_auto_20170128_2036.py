# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0042_auto_20170128_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modality',
            name='is_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modality',
            name='is_word',
            field=models.BooleanField(default=False),
        ),
    ]