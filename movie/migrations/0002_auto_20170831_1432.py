# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u7535\u5f71\u540d'),
        ),
    ]
