from django.shortcuts import render
from .models import *


def unifiedmodel_list(request):
    unified_models = UnifiedModel.objects.all()
    return render(request, 'unifiedmodel_list.html', {'unified_models': unified_models})