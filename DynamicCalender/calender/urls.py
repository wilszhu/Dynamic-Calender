from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('feed/', views.feed_page, name='feed'),
    path('calendar/', views.calendar_page, name = 'calendar'),
<<<<<<< HEAD
    path('wellness/', views.wellness, name = 'wellness'),
=======
    path('wellness/', views.wellness, name = 'wellness'),\
>>>>>>> 100466968b46dd166b7012f4f6cda480525e993e
]