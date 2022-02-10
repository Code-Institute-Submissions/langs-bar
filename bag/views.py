from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A View to return the bag.html """
    return render(request, 'bag/bag.html')
