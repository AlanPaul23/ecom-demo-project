from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
      # request is handled using HttpResponse object
    #return HttpResponse("Any kind of HTML Here")
    return render(request, "index.html")