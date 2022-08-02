from .models import Events, Calender
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'start', 'end', 'calender']

class CalendarForm(ModelForm):
    class Meta:
        model = Calender
        fields = ['title', 'start', 'end']