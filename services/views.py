from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Services

#####
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
#####

def service_list(request):
    services = Services.objects.all() 
    return render(request,'services.html',{'services': services})

def service_unit(request,sid):
    services = (
        {'id': 1,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/desk.jpg'            
        },
        {'id': 2,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/building.jpg'            
        },
        {'id': 3,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/loft.jpg'            
        },
        {'id': 4,
         'name': 'Project Name',
         'description': 'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
         'image': 'img/minibus.jpeg'            
        }
    )
    return render(request,'services.html',{'services': services})

