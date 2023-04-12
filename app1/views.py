from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def  fristapp1(request):
    return HttpResponse('<h1>this is fristapp1<h1>')

def secondapp1(request):
    return HttpResponse('<h1><marquee>this is secondapp1</h1></marquee>') 

 