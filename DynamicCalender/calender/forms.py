from .models import Events, Calender
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['eventName','calender', 'start_date', 'end_date', 'start_time', 'end_time', 'description', 'selectedCategory', 'assignedDate' ]

class CalendarForm(ModelForm):
    class Meta:
        model = Calender
        fields = ['user','title', 'description', 'start_date', 'end_date', 'start_time', 'end_time']