# _*_ coding:utf-8 _*_
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.http import JsonResponse
from django.http import HttpResponse

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from ..models.month1journal import Month1Journal    #Праздничные дежурства
from ..models.month2journal import Month2Journal    #Отпуск
from ..models.month7journal import Month7Journal    #Субботы
from ..models.month8journal import Month8Journal    #Дежурства 8-00
from ..models.month11journal import Month11Journal  #Дежурства 11-00
from team.models import team as teammodel
from ..models.services import Services
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
                    journal = Month2journal.objects.get(worker=worker,date=month)
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
        
        def WorkerStatus(worker,jid,current_date,month):
            pass
        
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
                        
        setattr(journal, 'day%d' % current_date.day, present) 
        
        def valid_journal(jid,worker,month,day):
            error = ''
            if jid == '1':
                pass
            elif jid == '7':
                pass
            elif jid == '8':
                #Проверка дежурного в другом журнале
                try:
                    jour = Month11Journal.objects.get(worker=worker,date=month)
                except Month11Journal.DoesNotExist:
                    jour = None
                    
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит на 11-00 !!! \nСделайте изменения в том журнале или назначте другого сотрудника."
                #Проверка дежурных в этом же журнале  
                try:
                    jour = Month8Journal.objects.all().filter(date=month)
                except Month8Journal.DoesNotExist:
                    jour = None
                for unit in jour:
                    present = unit and getattr(unit, 'day%s' % day, False)
                    if present:
                        if error == '':
                            error = u'Вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!' % unit.worker
                        else:
                            error = error + u'\nТакже вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s !' % unit.worker    
            elif jid == '11':
                #Проверка дежурного в другом журнале
                try:
                    jour = Month8Journal.objects.get(worker=worker,date=month)
                except Month8Journal.DoesNotExist:
                    jour = None
                
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит на 8-00 !!! \nСделайте изменения в том журнале или назначте другого сотрудника."                
                
                #Проверка дежурных в этом же журнале
                try:
                    jour = Month11Journal.objects.all().filter(date=month)
                except Month11Journal.DoesNotExist:
                    jour = None
                    
                for unit in jour:
                    present = unit and getattr(unit, 'day%s' % day, False)
                    if present:
                        if error == '':
                            error = u'Вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!' % unit.worker
                        else:
                            error = error + u'\nТакже вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s !' % unit.worker
            elif jid == '2':
                #Проверка сотрудника на дежурства
                #8-00
                try:
                    jour = Month8Journal.objects.get(worker=worker,date=month)
                except Month8Journal.DoesNotExist:
                    jour = None
                
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит на 8-00 !!!"
                #11-00    
                try:
                    jour = Month11Journal.objects.get(worker=worker,date=month)
                except Month11Journal.DoesNotExist:
                    jour = None
                
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит на 11-00 !!!"
                #Праздники
                try:
                    jour = Month1Journal.objects.get(worker=worker,date=month)
                except Month1Journal.DoesNotExist:
                    jour = None
                
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит в этот день !!!"
                
                #Субботы
                try:
                    jour = Month7Journal.objects.get(worker=worker,date=month)
                except Month7Journal.DoesNotExist:
                    jour = None
                
                present= jour and getattr(jour,'day%s' % day, False)
                if present:
                    error = u"Этот сотрудник дежурит в эту субботу !!!"
            else:
                pass
            
            return error
        
        error = ''
        if present:
            error = valid_journal(jid,worker,month,day)
        
        if not error:
            journal.save()
            
        return JsonResponse({'text':error}) 
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    