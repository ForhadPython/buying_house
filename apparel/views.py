from django.shortcuts import render
from .models import *


def apparels_view(request):
    banner = ApparelsBanner.objects.all()
    categories = ApparelsCategory.objects.all()
    genders = ApparelsGender.objects.all()

    # Filtering logic
    selected_category = request.GET.get('category')
    selected_gender = request.GET.get('gender')

    products = ApparelsProduct.objects.all()

    if selected_category:
        products = products.filter(category_id=selected_category)

    if selected_gender:
        products = products.filter(gender_id=selected_gender)

    context = {
        'banner': banner,
        'products': products,
        'categories': categories,
        'genders': genders,
        'selected_category': selected_category,
        'selected_gender': selected_gender,
    }
    return render(request, 'apparels.html', context)
