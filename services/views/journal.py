# _*_ coding:utf-8 _*_
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.http import JsonResponse
from django.http import HttpResponse

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from ..models.month8journal import Month8Journal
from ..models.month11journal import Month11Journal
from team.models import team as teammodel
from ..util import paginate

class JournalView(TemplateView):
    template_name = 'journal.html'
    
    def get_context_data(self, **kwargs): 
        
        jid = self.request.GET.get('id')        
        if jid:
            jid=jid
        else:
            jid="8"
        context = super(JournalView, self).get_context_data(**kwargs)
        if self.request.GET.get('month'):
            month=datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month,1)
        next_month=date(month.year, month.month+1,1)
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
        
        queryset = teammodel.Team.objects.all().filter(is_duty=True).order_by('last_name')     
        update_url = reverse('journal')
        
        team = []
        for worker in queryset: 
            try:
                if jid=='1':
                    journal = None#Month8Journal.objects.get(worker=worker,date=month)
                elif jid=='7':
                    journal = None#Month8Journal.objects.get(worker=worker,date=month)
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
        return context
    
    def post(self, request, *args, **kwargs):
        data = request.POST  
        #iid=data['iid']
        jid=data['jid']
        print(jid)
        current_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        month = date(current_date.year, current_date.month,1)
        present = data['present'] and True or False        
        worker = teammodel.Team.objects.get(pk=data['pk'])
        
        if jid=='11':
            journal = Month11Journal.objects.get_or_create(worker=worker,date=month)[0]
        elif journal=='1':                   
            jid= Month11Journal.objects.get_or_create(worker=worker,date=month)[0]
        else:
            journal = Month8Journal.objects.get_or_create(worker=worker,date=month)[0]
        
        setattr(journal, 'day%d' % current_date.day, present)
        journal.save()
        
        return JsonResponse({'status': 'success'})
    
    
    
    
    
    
    
    
    
    
    