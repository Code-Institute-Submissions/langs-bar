from django.shortcuts import render

# Create your views here.


def dresscode(request):
    """
    A View to return the events.html
    """
    return render(request, 'dresscode/dresscode.html')
