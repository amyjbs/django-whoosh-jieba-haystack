# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  movie.models import movie
# Create your views here.

def search(request,keys,var):

    result = movie.objects.all().filter(name__contains=keys)
    return render(request,'search.html',{'result':result,'var':var})

def search_whoosh(request):
    var = 1
    return  render(request,'whoosh.html',{'var':var})
