# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_auto_20170410_1315'),
        ('services', '0008_month11journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month1Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('day1', models.BooleanField(default=False)),
                ('day2', models.BooleanField(default=False)),
                ('day3', models.BooleanField(default=False)),
                ('day4', models.BooleanField(default=False)),
                ('day5', models.BooleanField(default=False)),
                ('day6', models.BooleanField(default=False)),
                ('day7', models.BooleanField(default=False)),
                ('day8', models.BooleanField(default=False)),
                ('day9', models.BooleanField(default=False)),
                ('day10', models.BooleanField(default=False)),
                ('day11', models.BooleanField(default=False)),
                ('day12', models.BooleanField(default=False)),
                ('day13', models.BooleanField(default=False)),
                ('day14', models.BooleanField(default=False)),
                ('day15', models.BooleanField(default=False)),
                ('day16', models.BooleanField(default=False)),
                ('day17', models.BooleanField(default=False)),
                ('day18', models.BooleanField(default=False)),
                ('day19', models.BooleanField(default=False)),
                ('day20', models.BooleanField(default=False)),
                ('day21', models.BooleanField(default=False)),
                ('day22', models.BooleanField(default=False)),
                ('day23', models.BooleanField(default=False)),
                ('day24', models.BooleanField(default=False)),
                ('day25', models.BooleanField(default=False)),
                ('day26', models.BooleanField(default=False)),
                ('day27', models.BooleanField(default=False)),
                ('day28', models.BooleanField(default=False)),
                ('day29', models.BooleanField(default=False)),
                ('day30', models.BooleanField(default=False)),
                ('day31', models.BooleanField(default=False)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team', unique_for_month=b'date', verbose_name='\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a \u0434\u0435\u0436\u0443\u0440\u0441\u0442\u0432 \u043f\u043e \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u043a\u0430\u043c',
                'verbose_name_plural': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0436\u0443\u0440\u043d\u0430\u043b\u044b \u043f\u043e \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u043a\u0430\u043c',
            },
        ),
        migrations.CreateModel(
            name='Month7Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('day1', models.BooleanField(default=False)),
                ('day2', models.BooleanField(default=False)),
                ('day3', models.BooleanField(default=False)),
                ('day4', models.BooleanField(default=False)),
                ('day5', models.BooleanField(default=False)),
                ('day6', models.BooleanField(default=False)),
                ('day7', models.BooleanField(default=False)),
                ('day8', models.BooleanField(default=False)),
                ('day9', models.BooleanField(default=False)),
                ('day10', models.BooleanField(default=False)),
                ('day11', models.BooleanField(default=False)),
                ('day12', models.BooleanField(default=False)),
                ('day13', models.BooleanField(default=False)),
                ('day14', models.BooleanField(default=False)),
                ('day15', models.BooleanField(default=False)),
                ('day16', models.BooleanField(default=False)),
                ('day17', models.BooleanField(default=False)),
                ('day18', models.BooleanField(default=False)),
                ('day19', models.BooleanField(default=False)),
                ('day20', models.BooleanField(default=False)),
                ('day21', models.BooleanField(default=False)),
                ('day22', models.BooleanField(default=False)),
                ('day23', models.BooleanField(default=False)),
                ('day24', models.BooleanField(default=False)),
                ('day25', models.BooleanField(default=False)),
                ('day26', models.BooleanField(default=False)),
                ('day27', models.BooleanField(default=False)),
                ('day28', models.BooleanField(default=False)),
                ('day29', models.BooleanField(default=False)),
                ('day30', models.BooleanField(default=False)),
                ('day31', models.BooleanField(default=False)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team', unique_for_month=b'date', verbose_name='\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a \u0434\u0435\u0436\u0443\u0440\u0441\u0442\u0432 \u043f\u043e \u0421\u0443\u0431\u0431\u043e\u0442\u0430\u043c',
                'verbose_name_plural': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0436\u0443\u0440\u043d\u0430\u043b\u044b \u043f\u043e \u0421\u0443\u0431\u0431\u043e\u0442\u0430\u043c',
            },
        ),
    ]
