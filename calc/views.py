from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
      # request is handled using HttpResponse object
    #return HttpResponse("Any kind of HTML Here")
    return render(request, "home.html",{'name':'Alan'})

def add(request):
    
    var1 =int(request.GET['num1'])
    var2 =int(request.GET['num2'])

    result = var1 + var2 
    return render(request, "result.html",{"result" : result})