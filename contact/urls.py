from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views

urlpatterns = [
    path('contact/', contact_view, name="contact")
]