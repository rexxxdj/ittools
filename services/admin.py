# _*_ coding:utf-8 _*_

from django.contrib import admin
from models import Services, Month1Journal, Month2Journal,Month7Journal, Month8Journal, Month11Journal

# Register your models here.
admin.site.register(Services)
admin.site.register(Month1Journal)
admin.site.register(Month2Journal)
admin.site.register(Month7Journal)
admin.site.register(Month8Journal)
admin.site.register(Month11Journal)
