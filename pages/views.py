from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.choices import bedroom_choices,price_choices,state_choices
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings':listings,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices
    }
    return render(request, template_name='pages/index.html',context = context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get mvp realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(request, template_name='pages/about.html', context=context)