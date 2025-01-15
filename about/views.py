from django.shortcuts import render
from .models import AboutBanner, About


def about_page(request):
    about_banner = AboutBanner.objects.first()  # Get the first About Banner
    about_items = About.objects.all()  # Get all About sections

    context = {
        'about_banner': about_banner,
        'about_items': about_items
    }

    return render(request, 'about.html', context)
