from django.shortcuts import render
from .models import HomeTexBanner, HomeTexData
from metadata.models import UnifiedModel


def home_tex_page(request):
    banners = HomeTexBanner.objects.all()
    home_tex = HomeTexData.objects.all()
    unified_model = UnifiedModel.objects.last()  # Assuming only one unified model

    context = {
        'banners': banners,
        'home_tex': home_tex,
        'unified_model': unified_model if unified_model else None,  # Only pass if it exists
    }
    return render(request, 'home-tex.html', context)
