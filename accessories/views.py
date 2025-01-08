from django.shortcuts import render
from .models import AccessoriesBanner, AccessoriesData


def accessories_page(request):
    # Fetch all data from AccessoriesBanner and AccessoriesData
    banners = AccessoriesBanner.objects.all()
    accessories = AccessoriesData.objects.all()
    context = {
        'banners': banners,
        'accessories': accessories,
    }
    return render(request, 'accessories.html', context)
