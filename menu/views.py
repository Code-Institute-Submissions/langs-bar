from django.shortcuts import render

# Create your views here.


def menu(request):
    """ A View to return the menu.html """
    return render(request, 'menu/menu.html')
