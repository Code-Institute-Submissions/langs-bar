from django.shortcuts import render

# Create your views here.


def contact(request):
    """ A View to return the index.html """
    return render(request, 'contact/contact.html')
