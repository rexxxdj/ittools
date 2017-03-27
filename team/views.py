from django.shortcuts import render

def main_page(request):
    return render(request,'team/index.html',{})

def team_list(request):
    return render(request,'team/team.html',{})