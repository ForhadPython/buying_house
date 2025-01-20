from django.urls import path
from . import views

urlpatterns = [
    path('unifiedmodel_list', views.unified_model_list, name='unifiedmodel_list'),
]