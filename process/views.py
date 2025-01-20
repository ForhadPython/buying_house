# views.py
from django.shortcuts import render
from .models import ProcessBanner, ProcessContent, ProcessData
from metadata.models import UnifiedModel


def process_page(request):
    process_banner = ProcessBanner.objects.first()  # Get the first banner
    process_content = ProcessContent.objects.all()  # Get all content items
    process_data = ProcessData.objects.all()  # Get all data items
    unified_model = UnifiedModel.objects.last()

    context = {
        'process_banner': process_banner,
        'process_content': process_content,
        'unified_model': unified_model,
        'process_data': process_data
    }

    return render(request, 'process.html', context)
