# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0005_auto_20170828_1223'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movie',
        ),
    ]
