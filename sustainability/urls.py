from django.urls import path
from .views import sustainability_view

urlpatterns = [
    path('sustainability/', sustainability_view, name='sustainability'),
]
