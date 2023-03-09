from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def yasdan(request):
    return HttpResponse('<h1>his my bother</h1>')


def sana(request):
    return HttpResponse('<marquee><h1>she is very very cute baby</h1></marquee>')

