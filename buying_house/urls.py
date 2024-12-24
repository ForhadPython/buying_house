"""
URL configuration for buying_house project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Home app
    path('', include('services.urls')),  # Services app
    path('', include('product.urls')),  # Product app
    path('', include('sustainability.urls')),  # Sustainability app
    path('', include('global_network.urls')),  # Global Network app
    path('', include('contact.urls')),  # Contact app
    path('', include('apparel.urls')),  # Apparel app
    path('', include('accessories.urls')),  # Accessories app
    path('', include('process.urls')),  # Process app
    path('', include('about.urls')),  # About app
    path('', include('metadata.urls')),  # About app
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
