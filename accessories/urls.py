from django.urls import path
from . import views

urlpatterns = [
    path('accessories/', views.accessories_page, name='accessories'),
]