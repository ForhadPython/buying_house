# views.py
from django.shortcuts import render
from .models import ProcessBanner, ProcessContent, ProcessData


def process_page(request):
    process_banner = ProcessBanner.objects.first()  # Get the first banner
    process_content = ProcessContent.objects.all()  # Get all content items
    process_data = ProcessData.objects.all()  # Get all data items

    context = {
        'process_banner': process_banner,
        'process_content': process_content,
        'process_data': process_data
    }

    return render(request, 'process.html', context)
