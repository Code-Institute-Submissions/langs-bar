from django.shortcuts import render

# Create your views here.


def about(request):
    """ A View to return the about.html """
    return render(request, 'about/about.html')
