from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('feed/', views.feed_page, name='feed'),
    path('calendar/', views.calendar_page, name = 'calendar'),
    path('wellness/', views.wellness, name = 'wellness'),
]