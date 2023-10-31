import re
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from scraper.class_search import find_class_data
from django.contrib.auth.forms import UserCreationForm

def index(request):
    class_details = None
    if request.method == 'POST':
        class_data = request.POST['search'].split()
        class_details = find_class_data(class_data[0], class_data[1])
        if class_details.strip().startswith('for'):
            class_details = 'No class found'
    return render(request, 'scraper/index.html', {'class_details': class_details})


def login_user(request):
    print("reached")
    if request.method == 'POST':
        print("reached2")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'scraper/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()
    return render(request, 'scraper/register.html', {'form': form})