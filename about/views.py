from django.shortcuts import render


def about(request):
    """ A View to return the about.html """
    return render(request, 'about/about.html')


def privacy(request):
    """ A View to return the privacy.html """
    return render(request, 'about/privacy.html')
