from django.shortcuts import render
from .models import GlobalBanner, GlobalNetwork, GlobalNetworkData

def global_network_view(request):
    # Fetch single banner for the header
    banner = GlobalBanner.objects.first()
    # Fetch the global network title and description
    global_network = GlobalNetwork.objects.first()
    # Fetch all global network data (e.g., features)
    global_network_data = GlobalNetworkData.objects.all()
    context = {
        'banner': banner,
        'global_network': global_network,
        'global_network_data': global_network_data,
    }
    return render(request, 'global-network.html', context)
