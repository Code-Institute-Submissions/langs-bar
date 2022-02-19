from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Event, Month

# Create your views here.


def all_events(request):
    """ A View to return the events.html """

    events = Event.objects.all()
    months = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower("name"))
            if sortkey == 'month':
                sortkey = 'month__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            events = events.order_by(sortkey)

        if 'month' in request.GET:
            months = request.GET['month'].split(',')
            events = events.filter(month__name__in=months)
            months = Month.objects.filter(name__in=months)

    current_sorting = f'{sort}_{direction}'

    context = {
        'events': events,
        'current_months': months,
        'current_sorting': current_sorting
    }

    return render(request, 'events/events.html', context)

def event_detail(request, event_id):
    """ A View to return an individual event details """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event
    }
    return render(request, 'events/event_detail.html', context)

def all_vip(request):
    """ A View to return the events.html """

    events = Event.objects.all()
    months = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower("name"))
            if sortkey == 'month':
                sortkey = 'month__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            events = events.order_by(sortkey)

        if 'month' in request.GET:
            months = request.GET['month'].split(',')
            events = events.filter(month__name__in=months)
            months = Month.objects.filter(name__in=months)

    current_sorting = f'{sort}_{direction}'

    context = {
        'events': events,
        'current_months': months,
        'current_sorting': current_sorting
    }

    return render(request, 'events/vip.html', context)

def vip_detail(request, event_id):
    """ A View to return an individual event details """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event
    }
    return render(request, 'events/vip_detail.html', context)
