from django.shortcuts import render

# Create your views here.


def vip(request):
    """ A View to return the index.html """
    return render(request, 'vip/vip.html')
