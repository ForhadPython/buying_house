from django.shortcuts import render
from .models import SustainabilityBanner, SustainabilityAbout, OurPartner, OurPartnerSlider
from metadata.models import UnifiedModel


def sustainability_view(request):
    # Fetch only the first record of SustainabilityBanner, assuming it's a single banner
    sustain_banner = SustainabilityBanner.objects.first()  # Only one banner is expected

    # Fetch all records for the other models
    sustain_data = SustainabilityAbout.objects.all()
    partner_desc = OurPartner.objects.first()  # Assuming one partner description
    partner_slider = OurPartnerSlider.objects.all()
    unified_model = UnifiedModel.objects.last()

    # Context to pass to the template
    context = {
        'sustain_banner': sustain_banner,
        'sustain_data': sustain_data,
        'partner_desc': partner_desc,
        'partner_slider': partner_slider,
        'unified_model': unified_model,
    }

    # Render the template with context
    return render(request, 'sustainability.html', context)
