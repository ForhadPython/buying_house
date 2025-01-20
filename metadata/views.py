from django.shortcuts import render
from .models import *


# Function-based view to display a list of UnifiedModel entries
def unified_model_list(request):
    unified_model = UnifiedModel.objects.last()  # Fetch the latest UnifiedModel entry
    return render(request, 'base.html', {'unified_model': unified_model})