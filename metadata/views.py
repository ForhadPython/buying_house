from django.shortcuts import render
from .models import *


def meta_footer(request):
    about_company = AboutCompany.objects.first()  # Assuming only one object
    important_links = ImportantLink.objects.all()
    contact_info = ContactInfo.objects.first()  # Assuming only one object
    footer_maps = FooterMaps.objects.all()

    context = {
        'about_company': about_company,
        'important_links': important_links,
        'contact_info': contact_info,
        'footer_maps': footer_maps,
    }
    return render(request, 'base.html', context)
