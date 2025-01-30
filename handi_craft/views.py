from django.shortcuts import render
from .models import HandiCraftBanner, HandiCraftData
from metadata.models import UnifiedModel


def handi_craft_page(request):
    banners = HandiCraftBanner.objects.all()
    handicrafts = HandiCraftData.objects.all()
    unified_model = UnifiedModel.objects.last()  # Assuming only one unified model

    context = {
        'banners': banners,
        'handicrafts': handicrafts,  # Fixed variable name
        'unified_model': unified_model,
    }
    return render(request, 'handi-craft.html', context)
