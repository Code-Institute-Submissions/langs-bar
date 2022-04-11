from django.shortcuts import render


def dresscode(request):
    """
    A View to return the events.html
    """
    return render(request, 'dresscode/dresscode.html')
