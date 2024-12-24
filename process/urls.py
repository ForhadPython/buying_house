# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_page, name='process_page'),
]
