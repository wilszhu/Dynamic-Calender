from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class events(models.Model):
    #The name of event
    eventName=models.CharField(max_length=200)
    #assignedDate #The time scheduled for the event
    def __str__(self):
        return self.eventName #Returns the name of event in string, human readable form
    #def recentEvent #This function is to tell whether the evnet will occur recently