from django.urls import path
from . import views

urlpatterns = [
    path('hometex/', views.home_tex_page, name='hometex'),
]
