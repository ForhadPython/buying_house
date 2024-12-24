from django.shortcuts import render
from .models import ProductBanner, ProductAbout

def product_page(request):
    # Fetch all ProductBanner and ProductAbout data
    banners = ProductBanner.objects.all()
    about_products = ProductAbout.objects.all()
    context = {
        'banners': banners,
        'about_products': about_products,
    }
    return render(request, 'product.html', context)
