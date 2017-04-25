# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20170425_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='location',
            field=models.CharField(choices=[('KH', '\u0425\u0430\u0440\u044c\u043a\u043e\u0432'), ('PL', '\u041f\u043e\u043b\u0442\u0430\u0432\u0430'), ('CH', '\u0427\u0435\u0440\u043d\u0438\u0433\u043e\u0432'), ('SM', '\u0421\u0443\u043c\u044b'), ('KR', '\u041a\u0440\u0435\u043c\u0435\u043d\u0447\u0443\u0433'), ('DN', '\u0414\u043d\u0435\u043f\u0440'), ('ZH', '\u0416\u0438\u0442\u043e\u043c\u0438\u0440'), ('VN', '\u0412\u0438\u043d\u043d\u0438\u0446\u0430'), ('CHERK', '\u0427\u0435\u0440\u043a\u0430\u0441\u0441\u044b'), ('KD', '\u041a\u0438\u0440\u043e\u0432\u043e\u0433\u0440\u0430\u0434'), ('HN', '\u0425\u0435\u0440\u0441\u043e\u043d'), ('NK', '\u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432'), ('UM', '\u0423\u043c\u0430\u043d\u044c'), ('KY', '\u041a\u0438\u0435\u0432'), ('LV', '\u041b\u044c\u0432\u043e\u0432')], default='KH', max_length=2, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
    ]
