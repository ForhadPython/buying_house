from django.shortcuts import render
from .models import ProductBanner, ProductAbout
from metadata.models import UnifiedModel

def product_page(request):
    # Fetch all ProductBanner and ProductAbout data
    banners = ProductBanner.objects.all()
    about_products = ProductAbout.objects.all()
    unified_model = UnifiedModel.objects.last()

    context = {
        'banners': banners,
        'about_products': about_products,
        'unified_model': unified_model,
    }
    return render(request, 'product.html', context)
