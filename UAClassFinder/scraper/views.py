import re
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from scraper.class_search import find_class_data
from django.contrib.auth.forms import UserCreationForm
from scraper.models import Course, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    class_details = ''
    if request.method == 'POST':
        class_data = request.POST['search'].split()
        if len(class_data) >= 2:
            class_details = find_class_data(class_data[0], class_data[1])
            if class_details[0].strip().startswith('for'):
                class_details = 'No class found'
                messages.error(request, f"Invalid class name.")
                return render(request, 'scraper/index.html', {'class_details': ''})
            return render(request, 'scraper/index.html', {'class_details': class_details[0]})
        else:
            messages.error(request, f"Invalid class name. Class name must be in the format 'CS 110'.")
    return render(request, 'scraper/index.html', {'class_details': class_details})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, f"Invalid username or password.")
            return redirect('login')
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

@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        class_name = request.POST['class_name']
        print(class_name)
        if class_name:
            #check if class exists in database
            try:
                course = Course.objects.get(class_name=class_name)
            except Course.DoesNotExist:
                #if not, scrape and add to database
                try:
                    find_class_data(class_name.split()[0], class_name.split()[1])
                except IndexError:
                    messages.error(request, f"Invalid class name.")
                    return redirect('dashboard')
                return redirect('dashboard')
            #add class to user profile
            user_profile.saved_courses.add(course)
            messages.success(request, f"Class '{class_name}' added successfully.")
            return redirect('dashboard')
                
    return render(request, 'scraper/dashboard.html', {'subscribed_classes': user_profile.saved_courses.all()})

def change_email(request):
    if request.method == 'POST':
        new_email = request.POST['email']
        if new_email:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.email = new_email
            user_profile.save()
            messages.success(request, f"Email changed to '{new_email}' successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, f"Invalid email.")
            return redirect('dashboard')
    return render(request, 'scraper/change_email.html')