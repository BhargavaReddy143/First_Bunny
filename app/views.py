from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sam(request):
    return HttpResponse('<h1><marquee>hiiiii banny!!!</marquee></h1>')

def raja(request):
    return HttpResponse('Hiii chintuuu!!')    