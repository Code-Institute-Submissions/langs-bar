from django.shortcuts import render
from .models import MenuImages

# Create your views here.


def menu(request):
    """ A View to return the vip booths to vip.html """
    menus = MenuImages.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'menu/menu.html', context)
