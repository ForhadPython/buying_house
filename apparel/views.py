from django.shortcuts import render
from .models import *

def apparels_view(request):
    banner =ApparelsBanner.objects.all()
    products = ApparelsProduct.objects.all()
    categories = ApparelsCategory.objects.all()
    genders = ApparelsGender.objects.all()
    context = {
        'banner': banner,
        'products': products,
        'categories': categories,
        'genders': genders,
    }
    return render(request, 'apparels.html', context)
