from django.shortcuts import render
from .models import MenuImages


def menu(request):
    """
    A View to return the menu.html
    where all menu images are returned
    in a carousel.
    """
    menus = MenuImages.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'menu/menu.html', context)
