from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hero(request):
    return HttpResponse('Hiiiii sample!!!1')

def rani(request):
    return HttpResponse('<marquee>hello raniiii!!!</marquee>')