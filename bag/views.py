from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from events.models import Event


# Create your views here.


def view_bag(request):
    """ A View to return the bag.html """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified event to the shopping bag """

    event = get_object_or_404(Event, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
        messages.success(request, f"Updated {event.name} in your bag.")
    else:
        bag[item_id] = quantity
        messages.success(request, f"Added {event.name} to your bag.")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified event to the specified amount"""

    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, "Updated quantity in your bag.")
    else:
        bag.pop(item_id)
        messages.success(request, "Updated quantity in your bag.")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    event = get_object_or_404(Event, pk=item_id)

    try:
        bag = request.session.get("bag", {})
        bag.pop(item_id)
        messages.success(request, f"Removed {event.name} from your bag.")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
