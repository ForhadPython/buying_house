from django.shortcuts import render
from .models import AccessoriesBanner, AccessoriesData
from metadata.models import UnifiedModel


def accessories_page(request):
    # Fetch all data from AccessoriesBanner and AccessoriesData
    banners = AccessoriesBanner.objects.all()
    accessories = AccessoriesData.objects.all()
    unified_model = UnifiedModel.objects.last()
    context = {
        'banners': banners,
        'accessories': accessories,
        'unified_model': unified_model,
    }
    return render(request, 'accessories.html', context)
