# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_doctor_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.IntegerField(default=1, verbose_name='挂号费'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='intro',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='医生简介'),
        ),
    ]
