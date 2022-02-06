from django.shortcuts import render

# Create your views here.


def location(request):
    """ A View to return the location.html """
    return render(request, 'location/location.html')
