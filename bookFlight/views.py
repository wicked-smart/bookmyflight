from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello, prem ! again...')


def hello(request, name):
    return HttpResponse('Hello' + name)