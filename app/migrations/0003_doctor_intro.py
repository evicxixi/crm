# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181126_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='intro',
            field=models.CharField(max_length=64, null=True, verbose_name='科室简介'),
        ),
    ]
