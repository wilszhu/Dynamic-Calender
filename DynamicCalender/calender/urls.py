from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/',
                                  permanent=False)),
    path('home/', views.home, name='home'),
    path('feed/', views.feed_page, name='feed'),
    path('calendar/', views.calendar_page, name = 'calendar'),
    path('wellness/', views.wellness, name = 'wellness'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_calendar/', views.add_calendar , name='add_calendar'),
    path('display_events/', views.display_events, name='display_events')
    
]