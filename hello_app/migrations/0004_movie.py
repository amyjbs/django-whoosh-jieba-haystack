# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0003_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('directors', models.CharField(max_length=20)),
                ('rate', models.FloatField()),
                ('website', models.URLField()),
            ],
        ),
    ]
