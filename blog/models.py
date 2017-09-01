# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200,verbose_name=u'标题',blank=True,null=True)
    content = models.TextField(blank=True,null=True,verbose_name=u'内容')
    def __unicode__(self):
        return "%s,%s" %(self.title,self.content)
    class Meta:
        verbose_name=u'新闻'


