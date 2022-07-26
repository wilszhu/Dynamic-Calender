from django.shortcuts import render
from .models import Events, Calender
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'calendar/templates/home.html')
        else:
            return render(request, 'calendar/templates/login.html')
    else:
        return render(request, 'calendar/templates/login.html')

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