from django.shortcuts import render
from django.http import HttpResponse

def team_list(request):
    team = (
        {'id': 1,
         'first_name': u'Ben',
         'last_name': u'Johnson',
         'position': u'Musician',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/1.jpg'},
        {'id': 2,
         'first_name': u'Emily',
         'last_name': u'Clark',
         'position': u'Artist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/2.jpg'},
        {'id': 3,
         'first_name': u'Carl',
         'last_name': u'Kent',
         'position': u'Stylist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/3.jpg'}
    )
    return render(request,'team.html',{'team': team})

def team_unit(request,uid):
    team = (
        {'id': 1,
         'first_name': u'Ben',
         'last_name': u'Johnson',
         'position': u'Musician',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/1.jpg'},
        {'id': 2,
         'first_name': u'Emily',
         'last_name': u'Clark',
         'position': u'Artist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/2.jpg'},
        {'id': 3,
         'first_name': u'Carl',
         'last_name': u'Kent',
         'position': u'Stylist',
         'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',         
         'image':'img/3.jpg'}
    )
    return render(request,'team.html',{'team': team})