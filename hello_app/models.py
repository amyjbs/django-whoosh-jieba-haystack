# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city =models.CharField(max_length=10)
    country =models.CharField(max_length=10)
    website =models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    F_n= models.CharField(max_length=10)
    L_n =models.CharField(max_length=10)
    email =models.EmailField()

    def __unicode__(self):
        return u"%s %s" %(self.F_n,self.F_n)
class Books(models.Model):
    titles = models.CharField(max_length=50)
    authors =models.ManyToManyField(Author)
    publisher =models.ForeignKey(Publisher)
    pub_date = models.DateField()

    def __unicode__(self):
        return self.titles






