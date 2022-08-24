from unicodedata import category
from django.db import models
import datetime
from django.utils import timezone
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
    class Meta:
        fields = ('start', 'end', 'title')
    #The name of event
    eventName=models.CharField(max_length=200)
    #Calender that the event belongs to
    calender = models.ForeignKey(Calender, on_delete=models.CASCADE)
    #The start date of the event
    start_date = models.DateField()
    #The end date of the event
    end_date = models.DateField()
    #The start time of the event
    start_time = models.TimeField()
    #The end time of the event
    end_time = models.TimeField()
    #The description of the event
    description=models.CharField(max_length=500)
    #The category of the event
    CATEGORY_OPTIONS=(
        ("a","Academics"),
        ("s","Sports"),
        ("e","Entertainment"),
        ("w","Work"),
        ("fam","Family"),
        ("sg","Self-growth"),
        ("fri","Friend"),
        ("shop","Shopping"),
        ("h","Health"),
        ("t","Travel")
    )
    selectedCategory=models.CharField(max_length=4,choices=CATEGORY_OPTIONS,blank=False,null=False)
    #assignedDate #The time scheduled for the event
    assignedDate=models.DateTimeField()
    def __str__(self):
        return self.eventName #Returns the name of event in string, human readable form
    #def recentEvent #This function is to tell whether the evnet will occur recently
    def recentEvent(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.assignedDate<=now
    class Meta:
        ordering = ['-assignedDate']
