# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50,verbose_name='电影名')
    directors = models.CharField(max_length=20,blank=True)
    rate = models.FloatField()
    website = models.URLField()


    def __unicode__(self):#return web result
        # return "{0}, {1}".format(self.name, self.directors)
        return "%s,%s,%s" %(self.name, self.directors,self.rate)



