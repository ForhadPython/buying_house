from django.urls import path
from . import views

urlpatterns = [
    path('handi-craft/', views.handi_craft_page, name='handi_craft'),
]
