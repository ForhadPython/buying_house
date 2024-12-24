from django.urls import path
from . import views

urlpatterns = [
    path('meta_footer/', views.meta_footer, name='meta_footer'),  # Adjust the URL name as needed
]
