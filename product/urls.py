from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_page, name='product_page'),
]
