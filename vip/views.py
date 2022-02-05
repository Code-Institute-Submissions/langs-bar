from django.shortcuts import render
from .models import Booth

# Create your views here.


def vip(request):
    """ A View to return the vip booths to vip.html """
    booths = Booth.objects.all()
    context = {
        'booths': booths
    }
    return render(request, 'vip/vip.html', context)
