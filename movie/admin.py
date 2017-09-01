# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from movie.models import movie
# Register your models here.
@admin.register(movie)
class movieAdmin(admin.ModelAdmin):
    list_display = ('name','rate','directors','website')
    list_filter = ('directors',)
    search_fields = ['name','directors',]


