# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20170425_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='location',
            field=models.CharField(choices=[('KH', '\u0425\u0430\u0440\u044c\u043a\u043e\u0432'), ('PL', '\u041f\u043e\u043b\u0442\u0430\u0432\u0430')], default='KH', max_length=2, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
    ]
