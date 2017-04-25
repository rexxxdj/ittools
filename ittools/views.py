# _*_ coding:utf-8 _*_
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from services.models.services import Services

def index_list(request):
    return redirect('/services/')
    #services = Services.objects.all() 
    #return render(request,'index.html',{'services': services})