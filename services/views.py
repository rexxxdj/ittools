from django.shortcuts import render

def main_page(request):
    return render(request,'services/index.html',{})

def service_list(request):
    return render(request,'services/services.html',{})