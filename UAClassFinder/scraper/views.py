from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from scraper.class_search import find_class_data
from django.template import context, loader

def index(request):
    class_details = None
    if request.method == 'POST':
        print("printing----", request.POST['search'])
        class_data = request.POST['search'].split()
        class_details = find_class_data(class_data[0], class_data[1])
        print("printing----", class_details)
    return render(request, 'scraper/index.html', {'class_details': class_details})


def login(request):
    return render(request, 'scraper/login.html')