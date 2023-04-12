from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def firstapp2(request):
    return HttpResponse('<h1>this is firstapp2</h1>')     