from django.shortcuts import render

def team_list(request):
    return render(request,'team/team.html',{})