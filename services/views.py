from django.shortcuts import render
from services.models import ServiceBanner, ServiceData, WorkTogether


def services_page(request):
    service_banners = ServiceBanner.objects.first()  # Get the first banner (single object)
    service_data = ServiceData.objects.all()  # Fetch all service data
    first_service = ServiceData.objects.first()  # Fetch the first ServiceData object
    work_together = WorkTogether.objects.first()  # Fetch the first "work together" data

    context = {
        'service_banners': service_banners,  # single object, not queryset
        'service_data': service_data,
        'first_service': first_service,  # Pass the first service separately
        'work_together': work_together
    }

    return render(request, 'service.html', context)
