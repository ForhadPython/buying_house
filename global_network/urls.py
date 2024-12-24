from django.urls import path
from . import views

urlpatterns = [
    path('global_network/', views.global_network_view, name='global_network'),
]