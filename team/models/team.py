# _*_ coding: utf-8 _*_

from __future__ import unicode_literals
from django.db import models

class Team(models.Model):    
    """Team Model"""
    class Meta(object):
        verbose_name=u'Сотрудник'
        verbose_name_plural=u'Команда'
    
    first_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name = u'Имя')
    
    last_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name = u'Фамилия')
    
    middle_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name = u'Отчество',
        null=True)
    
    birthday = models.DateField(
        blank=False,
        verbose_name = u'Дата рождения',
        null=True)
    
    position = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u'Должность')
    
    photo = models.FileField(
        upload_to='img/team/',
        verbose_name = u'Фото min 320*320',
        blank=True,
        null=True)
    
    is_duty = models.BooleanField(
        blank=True,
        verbose_name=u'Дежурит',
        default=False)
    
    notes = models.TextField(
        blank=True,
        verbose_name=u'Дополнительная информация')
   
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)