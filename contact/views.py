from django.shortcuts import render, redirect
from .models import Contact, AdditionalInfo, BusinessHours, ContactBanner

def contact_view(request):
    message = None
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        if full_name and email and description:
            Contact.objects.create(full_name=full_name, email=email, description=description)
            message = "Thank you for getting in touch! We'll get back to you soon."
        else:
            message = "All fields are required. Please fill out the form completely."

    banner = ContactBanner.objects.first()  # Fetch the first banner
    additional_info = AdditionalInfo.objects.first()
    business_hours = BusinessHours.objects.first()

    context = {
        'banner': banner,
        'additional_info': additional_info,
        'business_hours': business_hours,
        'message': message,
    }
    return render(request, 'contact.html', context)


