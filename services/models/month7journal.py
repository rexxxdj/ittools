# _*_ coding: utf-8 _*_

from django.db import models
from team.models import team

class Month7Journal(models.Model):
    '''Work Mounthly Journal Субботы'''
    class Meta:
        verbose_name = u'Месячный график дежурств по Субботам'
        verbose_name_plural = u'Месячные журналы по Субботам'
        
    worker = models.ForeignKey('team.Team',
        verbose_name=u'Сотрудник',
        blank=False,
        unique_for_month='date')
    
    # we only need year and month, so always set day to first day of the month
    
    date = models.DateField(
        verbose_name = u'Дата',
        blank=False)
    
    day1 = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)
    day8 = models.BooleanField(default=False)
    day9 = models.BooleanField(default=False)
    day10 = models.BooleanField(default=False)
    day11 = models.BooleanField(default=False)
    day12 = models.BooleanField(default=False)
    day13 = models.BooleanField(default=False)
    day14 = models.BooleanField(default=False)
    day15 = models.BooleanField(default=False)
    day16 = models.BooleanField(default=False)
    day17 = models.BooleanField(default=False)
    day18 = models.BooleanField(default=False)
    day19 = models.BooleanField(default=False)
    day20 = models.BooleanField(default=False)
    day21 = models.BooleanField(default=False)
    day22 = models.BooleanField(default=False)
    day23 = models.BooleanField(default=False)
    day24 = models.BooleanField(default=False)
    day25 = models.BooleanField(default=False)
    day26 = models.BooleanField(default=False)
    day27 = models.BooleanField(default=False)
    day28 = models.BooleanField(default=False)
    day29 = models.BooleanField(default=False)
    day30 = models.BooleanField(default=False)
    day31 = models.BooleanField(default=False)       
    
    def __unicode__(self):
        return u'%s %s: %d, %d' % (self.worker.last_name, self.worker.first_name, self.date.month, self.date.year)
    
    
    