from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Calender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

class Events(models.Model):
    #The name of event

    #Calender that the event belongs to

    #The start date of the event

    #The end date of the event

    #The start time of the event

    #The end time of the event

    #The description of the event

    #The category of the event

    eventName=models.CharField(max_length=200)
    #assignedDate #The time scheduled for the event

    def __str__(self):
        return self.eventName #Returns the name of event in string, human readable form
    #def recentEvent #This function is to tell whether the evnet will occur recently

    class Meta:
        ordering = ['-assignedDate']