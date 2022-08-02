from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Events, Calender
from .forms import EventForm, CalendarForm

# Create your views here.
def feed_page(request):
    return render(request, 'feed.html')

def calendar_page(request):
    return render(request, 'calendar.html')

def wellness(request):
    return render(request, 'wellness.html')

def home(request):
    return render(request, 'home.html')

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

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar.html')
    else:
        form = EventForm()
    return render(request, 'calendar/templates/add_event.html', {'form': form})

def add_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar.html')
    else:
        form = CalendarForm()
    return render(request, 'calendar/templates/add_calendar.html', {'form': form})

def display_events(request):
    if request.method == 'GET':
        events = Events.objects.filter(calender__user=request.user, start__gte=datetime.now())
    return render(request, 'calendar/templates/display_events.html', {'events': events})
