from django.shortcuts import render


def index(request):
    """
    A View to return the index.html
    """
    return render(request, 'home/index.html')
