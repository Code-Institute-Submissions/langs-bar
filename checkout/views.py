from django.shortcuts import render

# Create your views here.


def checkout(request):
    """ A View to return the checkout.html """
    return render(request, 'checkout/checkout.html')
