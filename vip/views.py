from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Booth, MonthVip

# Create your views here.


def vip(request):
    """ A View to return the vip.html """

    booths = Booth.objects.all()
    query = None
    months = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                booths = booths.annotate(lower_name=Lower("name"))
            if sortkey == 'month':
                sortkey = 'month__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            booths = booths.order_by(sortkey)

        if 'month' in request.GET:
            months = request.GET['month'].split(',')
            booths = booths.filter(month__name__in=months)
            months = MonthVip.objects.filter(name__in=months)

    current_sorting = f'{sort}_{direction}'

    context = {
        'booths': booths,
        'current_months': months,
        'current_sorting': current_sorting
    }

    return render(request, 'vip/vip.html', context)

def vip_detail(request, booth_id):
    """ A View to return an individual booth details """
    booth = get_object_or_404(Booth, pk=booth_id)
    context = {
        'booth': booth
    }
    return render(request, 'vip/vip_detail.html', context)
