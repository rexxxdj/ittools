# _*_ coding:utf-8 _*_
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.http import JsonResponse
from django.http import HttpResponse
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView

from ..models.month1journal import Month1Journal    #Праздничные дежурства
from ..models.month2journal import Month2Journal    #Отпуск
from ..models.month7journal import Month7Journal    #Субботы
from ..models.month8journal import Month8Journal    #Дежурства 8-00
from ..models.month11journal import Month11Journal  #Дежурства 11-00
from team.models import team as teammodel
from ..models.services import Services
from ittools.utils.pagination import paginate
from ittools.utils.validation import valid_journal

class JournalView(TemplateView):
    template_name = 'journal.html'
     
       
    def get_context_data(self, **kwargs):         
        context = super(JournalView, self).get_context_data(**kwargs)
        
        jid = self.request.GET.get('id')  
        if jid:
            jid=jid
        else:
            jid="8"
        
        if self.request.GET.get('month'):
            month=datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month,1)
            
        if month.month==12:
            next_month=date(month.year+1,1,1)
        else:
            next_month=date(month.year, month.month+1,1)
        
        if month.month==1:
            prev_month=date(month.year-1, 12,1)  
        else:
            prev_month=date(month.year, month.month-1,1)  
        
        context['jid'] = jid
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')
        context['cur_month'] = month.strftime('%Y-%m-%d')
        
        
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear,mmonth)[1]
        context['month_header'] = [{'day': d,
            'verbose': day_abbr[weekday(myear,mmonth,d)][:2]}
            for d in range(1,number_of_days+1)]
        
        if jid == '8' or jid == '11':
            queryset = teammodel.Team.objects.all().filter(is_duty=True).order_by('last_name') 
        else:
            queryset = teammodel.Team.objects.all().order_by('-is_duty', 'last_name') 
        update_url = reverse('journal')
                
        team = []
        for worker in queryset: 
            
            try:
                if jid=='1':
                    journal = Month1Journal.objects.get(worker=worker,date=month)
                elif jid=='2':                    
                    journal = Month2Journal.objects.get(worker=worker,date=month)
                elif jid=='7':
                    journal = Month7Journal.objects.get(worker=worker,date=month)
                elif jid=='8':
                    journal = Month8Journal.objects.get(worker=worker,date=month)
                elif jid=='11':
                    journal = Month11Journal.objects.get(worker=worker,date=month)
            except Exception:
                journal=None   
                
            days = []
            for day in range (1,number_of_days+1):
                days.append({
                    'day': day,                  
                    'present': journal and getattr(journal,'day%d' % day, False), 
                    'verbose': day_abbr[weekday(myear,mmonth,day)][:2],
                    'date': date(myear,mmonth,day).strftime('%Y-%m-%d'),                   
                    'jid':jid,
                })
            team.append({
                'full_name': u'%s %s' % (worker.last_name, worker.first_name),
                'days': days,
                'id': worker.id,
                'update_url': update_url,                
            })            
        context = paginate(team, 10, self.request, context,var_name='team')
        
        services = []
        query = Services.objects.all()
        for service in query:
            services.append({
                'project_name': service.project_name,
                'link': service.link
            })
        context['services'] = services
        return context
    
    
    def post(self, request, *args, **kwargs):
        
        data = request.POST 
        jid=data['jid']
        current_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        month = date(current_date.year, current_date.month,1)
        present = data['present'] and True or False        
        worker = teammodel.Team.objects.get(pk=data['pk'])          
        day = data['day']               
        
        if jid=='11':
            journal = Month11Journal.objects.get_or_create(worker=worker,date=month)[0]
        elif jid=='1':                   
            journal = Month1Journal.objects.get_or_create(worker=worker,date=month)[0]
        elif jid=='2':
            journal = Month2Journal.objects.get_or_create(worker=worker,date=month)[0]
        elif jid =='7':
            journal = Month7Journal.objects.get_or_create(worker=worker,date=month)[0]
        else:
            journal = Month8Journal.objects.get_or_create(worker=worker,date=month)[0] 
        
        error = ''
        if present:
            error = valid_journal(jid,worker,month,day) 
        
        if not error:
            setattr(journal, 'day%d' % current_date.day, present) 
            journal.save()
            
        return JsonResponse({'text':error}) 
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    