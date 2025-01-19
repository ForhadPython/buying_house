from django.urls import path
from . import views

urlpatterns = [
    path('metadata/', views.unifiedmodel_list, name='unifiedmodel-list'),
]