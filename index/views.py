from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    second = '<h1>second project</h1>'
    return HttpResponse(second)