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
        default='')
    
    birthday = models.DateField(
        blank=False,
        verbose_name = u'Дата рождения',
        null=True)
    
    position = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u'Должность')
    
    photo = models.ImageField(
        blank=True,
        verbose_name=u'Фото',
        null=True),
    
    notes = models.TextField(
        blank=True,
        verbose_name=u'Дополнительная информация')
   
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    """team = (
        {'id': 1,
         'first_name': u'Ben',
         'last_name': u'Johnson',
         'position': u'Musician',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/1.jpg'},
        {'id': 2,
         'first_name': u'Emily',
         'last_name': u'Clark',
         'position': u'Artist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/2.jpg'},
        {'id': 3,
         'first_name': u'Carl',
         'last_name': u'Kent',
         'position': u'Stylist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/3.jpg'}
    )"""