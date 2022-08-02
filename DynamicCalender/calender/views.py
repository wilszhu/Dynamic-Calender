from django.shortcuts import render, redirect
from .models import Events, Calender
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def feed_page(request):
    return render(request, 'calender/templates/feed.html')

def calendar_page(request):
    return render(request, 'calendar/templates/calendar.html')

def wellness(request):
    return render(request, 'calendar/templates/wellness.html')

def home(request):
    return render(request, 'calendar/templates/home.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home.html')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'calendar/templates/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'calendar/templates/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return render(request, 'calendar/templates/login.html')