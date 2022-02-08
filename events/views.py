from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.


def all_events(request):
    """ A View to return the events.html """
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)

def event_detail(request, event_id):
    """ A View to return an individual event details """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event
    }
    return render(request, 'events/event_detail.html', context)
