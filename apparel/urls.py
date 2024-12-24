from django.urls import path
from .views import apparels_view

urlpatterns = [
    path('apparels/', apparels_view, name='apparels'),
]
