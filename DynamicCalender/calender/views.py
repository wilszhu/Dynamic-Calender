from django.shortcuts import render

# Create your views here.
def feed_page(request):
    return render(request, 'calender/templates/feed.html')

def calendar_page(request):
    return render(request, 'calendar/templates/calendar.html')

def wellness(request):
    return render(request, 'calendar/templates/wellness.html')

