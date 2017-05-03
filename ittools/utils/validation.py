# _*_ coding:utf-8 _*_
from services.models import *

def chek_journal(jid,worker,date,day,flag):
    '''jid - код журнала; worker -  id сотрудника; date - месяц; day - день; flag - если 1 - ищем по сотруднику, 0 - ищем всех дежурных'''    
    if jid == 1: 
        '''Праздники'''        
        if flag == 1:
            try:
                jour = Month1Journal.objects.get(worker=worker,date=date)
            except Month1Journal.DoesNotExist:
                jour = None
        else:
            try:
                jour = Month1Journal.objects.all().filter(date=date)
            except Month1Journal.DoesNotExist:
                jour = None
    elif jid == 2: 
        '''Отпуск'''
        if flag == 1:
            try:
                jour = Month2Journal.objects.get(worker=worker,date=date)
            except Month2Journal.DoesNotExist:
                jour = None
        else:
            try:
                jour = Month2Journal.objects.all().filter(date=date)
            except Month2Journal.DoesNotExist:
                jour = None
    elif jid == 7: 
        '''Субботы'''
        if flag == 1:
            try:
                jour = Month7Journal.objects.get(worker=worker,date=date)
            except Month7Journal.DoesNotExist:
                jour = None
        else:
            try:
                jour = Month7Journal.objects.all().filter(date=date)
            except Month7Journal.DoesNotExist:
                jour = None
    elif jid == 8: 
        '''8-00'''
        if flag == 1:
            try:
                jour = Month8Journal.objects.get(worker=worker,date=date)
            except Month8Journal.DoesNotExist:
                jour = None
        else:
            try:
                jour = Month8Journal.objects.all().filter(date=date)
            except Month8Journal.DoesNotExist:
                jour = None
    elif jid == 11: 
        '''11-00'''
        if flag == 1:
            try:
                jour = Month11Journal.objects.get(worker=worker,date=date)
            except Month11Journal.DoesNotExist:
                jour = None
        else:
            try:
                jour = Month11Journal.objects.all().filter(date=date)
            except Month11Journal.DoesNotExist:
                jour = None
                
    if flag == 1:
        present = jour and getattr(jour,'day%s' % day, False) 
        if present:
            return present
    else:
        for unit in jour:
            present = unit and getattr(unit,'day%s' % day, False)
            if present:
                return (unit.worker, present)
    
        
    #return present

def valid_journal(jid,worker,month,day): 
    errormsg =  {'error': u'%s дежурит в этот день !!!',
                 'universdate': u'%s дежурит на %s !!! \nСделайте изменения в том журнале или назначте другого сотрудника.',
                 'univers': u'Вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!',
                 'univers+': u'\nТакже вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!',
                 'journal': u'Вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!',
                 'journal2': u'\nТакже вы пытаетесь назначить второго сотрудника на дежурство в этот день. \nУже дежурным назначен %s!',
                 'otpusk': u'%s в отпуске!',
                 'otpusk+': u'\nТакже %s в отпуске!'}
    
    error = ''
    if jid == '1':
        pass
    elif jid == '7':
        pass
    elif jid == '8':
        #Проверка дежурного в другом журнале
        present = chek_journal(11,worker,month,day,1)
        if present:
            error = errormsg['universdate'] % (worker, '11-00')
            
        #Проверка дежурных в этом же журнале 
        present = chek_journal(8,worker,month,day,0)
        if present:
            if error == '':
                error  = errormsg['univers'] % present[0]
            else:
                error = error + errormsg['univers+'] % present[0]
                
        #Проверка дежурного в отпуске
        present = chek_journal(2,worker,month,day,1)        
        if present:
            if error == '':
                error = errormsg['otpusk'] % worker
            else:
                error = error + errormsg['otpusk+'] % worker
    elif jid == '11':
        #Проверка дежурного в другом журнале
        present = chek_journal(8,worker,month,day,1)        
        if present:
            error = errormsg['universdate'] % (worker, '8-00')
            
        #Проверка дежурных в этом же журнале
        present = chek_journal(11,worker,month,day,0)
        if present:
            if error == '':
                error = errormsg['journal'] % present[0]
            else:
                error = error + errormsg['journal2'] % present[0]       
        #Проверка дежурного в отпуске
        present = chek_journal(2,worker,month,day,1)        
        if present:
            if error == '':
                error = errormsg['otpusk'] % worker
            else:
                error = error + errormsg['univers+'] % present[0]
    elif jid == '2':
        #Проверка сотрудника на дежурства
        #8-00
        try:
            jour = Month8Journal.objects.get(worker=worker,date=month)
        except Month8Journal.DoesNotExist:
            jour = None
        
        present= jour and getattr(jour,'day%s' % day, False)
        if present:
            error = errormsg['universdate'] % (worker, '8-00')
        #11-00    
        try:
            jour = Month11Journal.objects.get(worker=worker,date=month)
        except Month11Journal.DoesNotExist:
            jour = None
        
        present= jour and getattr(jour,'day%s' % day, False)
        if present:
            error = errormsg['universdate'] % (worker, '11-00')
        #Праздники
        try:
            jour = Month1Journal.objects.get(worker=worker,date=month)
        except Month1Journal.DoesNotExist:
            jour = None
            
        present= jour and getattr(jour,'day%s' % day, False)
        if present:
            error = errormsg['error'] % worker
            
        #Субботы
        try:
            jour = Month7Journal.objects.get(worker=worker,date=month)
        except Month7Journal.DoesNotExist:
            jour = None
        
        present= jour and getattr(jour,'day%s' % day, False)
        if present:
            error = errormsg['error'] % worker
        else:
            pass
    return error