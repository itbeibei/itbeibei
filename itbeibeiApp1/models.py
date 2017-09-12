# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField('名字',max_length=30)

    class Meta:
        verbose_name = '测试专用'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
