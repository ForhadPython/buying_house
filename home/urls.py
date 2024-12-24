from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Adjust the URL name as needed
]
