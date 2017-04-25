# _*_ coding: utf-8 _*_

from __future__ import unicode_literals
from django.db import models

class Team(models.Model):  
    KHARKOV = 'Харьков'
    POLTAVA = 'Полтава'
    CHERNIGIV='Чернигов'
    SUMY='Сумы'
    KREMENCHUG='Кременчуг'
    DNIPRO='Днепр'
    ZHITOMYR='Житомир'
    VINNITSA='Винница'
    CHERKASSY='Черкассы'
    KRAPIVNITSKYI='Крапивницкий'
    KHERSON='Херсон'
    NIKOLAEV='Николаев'
    UMAN='Умань'
    KYIV='Киев'
    LVIV='Львов'
    
    LOCATIONS_CHOICES = (
        (KHARKOV, 'Харьков'), (POLTAVA, 'Полтава'), (CHERNIGIV, 'Чернигов'),
        (SUMY, 'Сумы'), (KREMENCHUG, 'Кременчуг'), (DNIPRO, 'Днепр'),
        (ZHITOMYR, 'Житомир'), (VINNITSA, 'Винница'), (CHERKASSY, 'Черкассы'),
        (KRAPIVNITSKYI, 'Крапивницкий'), (KHERSON, 'Херсон'), (NIKOLAEV, 'Николаев'),
        (UMAN, 'Умань'), (KYIV, 'Киев'), (LVIV, 'Львов'),
    )
    
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
        blank=True,
        verbose_name = u'Отчество',
        null=True)
    
    location = models.CharField(
        max_length=255,
        choices=LOCATIONS_CHOICES,
        default=KHARKOV,
        verbose_name = u'Город')
    
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=u'Телефоны')
    
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name = u'Email')
    
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