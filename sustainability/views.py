from django.shortcuts import render
from .models import SustainabilityBanner, SustainabilityAbout, OurPartner, OurPartnerSlider

def sustainability_view(request):
    # Fetch data from the database
    banners = SustainabilityBanner.objects.all()
    abouts = SustainabilityAbout.objects.all()
    partners = OurPartner.objects.all()
    partner_sliders = OurPartnerSlider.objects.all()

    # Context for the template
    context = {
        'banners': banners,
        'abouts': abouts,
        'partners': partners,
        'partner_sliders': partner_sliders,
    }
    return render(request, 'sustainability.html', context)
