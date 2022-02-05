from django.shortcuts import render

# Create your views here.


def events(request):
    """ A View to return the events.html """
    return render(request, 'events/events.html')
