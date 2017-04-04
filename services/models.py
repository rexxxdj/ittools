# _*_ coding: utf-8 _*_

from __future__ import unicode_literals
from django.db import models

class Services(models.Model):    
    """Team Model"""
    class Meta(object):
        verbose_name=u'Приложение'
        verbose_name_plural=u'Приложения'
    
    project_name = models.CharField(
        max_length=84,
        blank=False,
        verbose_name = u'Название')
    
    description = models.CharField(
        max_length = 255,
        blank = False,
        verbose_name=u'Краткое описание')
    
    photo = models.FileField(
        upload_to='img/services/',
        verbose_name = u'Фото 640*426',
        blank=True,
        null=True)
    
    link = models.CharField(
        max_length=1024,
        blank=False,
        verbose_name=u'Ссылка на приложение',
        null=True)
    
    notes = models.TextField(
        blank=True,
        verbose_name=u'Дополнительная информация')
   
    def __unicode__(self):
        return u'%s' % (self.project_name)