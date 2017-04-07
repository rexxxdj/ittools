# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse
from models import Team

def team_list(request):
    team = Team.objects.all()   
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

def worker_add(request):
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
            
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u'Имя обязательное'
            else:
                data['first_name'] = first_name
                
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u'Фамилия обязательна'
            else:
                data['last_name'] = last_name
                
            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u'Дата рождения обязательна'
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u'Введите корректный вормат даты'
                else:
                    data['birthday'] = birthday
                
            position = request.POST.get('position', '').strip()
            if not position:
                errors['position'] = u'Должность обязательна'
            else:
                data['position'] = position
                
            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo 
            
            if not errors:
                worker = Team(**data)
                worker.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request,'worker_add.html',{'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'worker_add.html',{})










