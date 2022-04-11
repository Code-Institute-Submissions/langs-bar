from django.shortcuts import render


def location(request):
    """
    A View to return the location.html
    """
    return render(request, 'location/location.html')
