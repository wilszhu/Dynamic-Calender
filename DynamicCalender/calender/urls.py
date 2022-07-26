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
    path('wellness/', views.wellness, name = 'wellness'),\
]