# views.py
from django.shortcuts import render
from .models import AboutBanner, About, SliderTitle, AboutSlider

def about_page(request):
    about_banner = AboutBanner.objects.first()  # Get the first About Banner
    about = About.objects.all()  # Get all About sections
    slider_title = SliderTitle.objects.first()  # Get the first slider title
    about_slider = AboutSlider.objects.all()  # Get all About Slider sections

    context = {
        'about_banner': about_banner,
        'about': about,
        'slider_title': slider_title,
        'about_slider': about_slider,
    }

    return render(request, 'about.html', context)
