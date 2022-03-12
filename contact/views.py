from django.shortcuts import render

# Create your views here.


def contact(request):
    """ A View to return the contact.html """
    return render(request, 'contact/contact.html')
