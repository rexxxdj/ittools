# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_team_is_duty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='is_duty',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u0436\u0443\u0440\u0438\u0442'),
        ),
    ]
