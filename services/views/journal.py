# _*_ coding:utf-8 _*_
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from ..models.month8journal import Month8Journal
from team.models import team as teammodel
from ..util import paginate

class JournalView(TemplateView):
    template_name = 'journal.html'
    
    def get_context_data(self, **kwargs):
        context = super(JournalView, self).get_context_data(**kwargs)
        
        if self.request.GET.get('month'):
            month=datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month,5)
        
        next_month=month + relativedelta(month=1)
        prev_month=month - relativedelta(month=1)        
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['prev_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')
        context['cur_month'] = month.strftime('%Y-%m-%d')
        
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear,mmonth)[1]
        context['month_header'] = [{'day': d,
            'verbose': day_abbr[weekday(myear,mmonth,d)][:2]}
            for d in range(1,number_of_days+1)]
        
        queryset = teammodel.Team.objects.all().order_by('last_name')#.filter(last_name=u'Токарь')        
        update_url = reverse('journal')
        
        team = []
        
        
        for worker in queryset: 
            try:
                journal = Month8Journal.objects.get(worker=worker,date=month)
            except Exception:
                journal=None            
            days = []
            for day in range (1,number_of_days+1):
                days.append({
                    'day': day,
                    #'present': journal and getattr(journal,'day%d' % day, False) or False,                    
                    'present': journal and getattr(journal,'day%d' % day, False),                    
                    'date': date(myear,mmonth,day).strftime('%Y-%m-%d'),
                })
            team.append({
                'full_name': u'%s %s' % (worker.last_name, worker.first_name),
                'days': days,
                'id': worker.id,
                'update_url': update_url,
            })            
        context = paginate(team, 10, self.request, context,var_name='team')   
        
        return context