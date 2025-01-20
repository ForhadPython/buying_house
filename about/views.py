from django.shortcuts import render
from .models import AboutBanner, About
from metadata.models import UnifiedModel


def about_page(request):
    about_banner = AboutBanner.objects.first()  # Get the first About Banner
    about_items = About.objects.all()  # Get all About sections
    unified_model = UnifiedModel.objects.last()

    context = {
        'about_banner': about_banner,
        'unified_model': unified_model,
        'about_items': about_items
    }

    return render(request, 'about.html', context)
