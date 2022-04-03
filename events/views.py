from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Event, Month
from .forms import EventForm

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
                sortkey = 'date'
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


@login_required
def add_event(request):
    """ Add a event to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. \
                Please ensure the form is valid.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit a event in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. \
                Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def confirm_delete(request, event_id):
    """ A Delete Event Confirmation View """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/confirm_delete.html', context)


@login_required
def delete_event(request, event_id):
    """ Delete a event from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))
