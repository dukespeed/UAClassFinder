from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader

def index(request):
    return render(request, 'scraper/index.html')

def login(request):
    return render(request, 'scraper/login.html')