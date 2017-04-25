from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from ..models.services import Services

def service_list(request):
    services = Services.objects.all() 
    return render(request,'services.html',{'services': services})

