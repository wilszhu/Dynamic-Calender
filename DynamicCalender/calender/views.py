from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime

from .models import Events, Calender
from .forms import EventForm, CalendarForm

# Create your views here.
def feed_page(request):
    return render(request, 'calendar/feed.html')

def calendar_page(request):
    return render(request, 'calendar/calendar.html')

def wellness(request):
    return render(request, 'calendar/wellness.html')

@login_required(login_url='login')
def home(request):
    calenders = Calender.objects.filter(user=request.user)
    context = {"calenders": calenders}
    return render(request, 'calendar/home.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'calendar/login.html', context)

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home')
    else:
        form = UserCreationForm()
    return render(request, 'calendar/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return render(request, 'calendar/login.html')

def add_event(request):
    current_user = request.user
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'calendar/add_event.html', {'form': form, 'current_user': current_user.id})

def add_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalendarForm()
    return render(request, 'calendar/add_calendar.html', {'form': form})

def display_events(request):
    if request.method == 'POST':
        pk = request.POST.get("events")
        calender = Calender.objects.get(pk=pk)
        events = Events.objects.filter(calender=calender)
    context = {'events': events}
    return render(request, 'calendar/display_events.html', context)
