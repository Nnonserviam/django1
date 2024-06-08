#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("WASAP!?")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("¿WASOP!")
    return render(request,'about.html')