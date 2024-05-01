from django.urls import path
from . import views

urlpatterns = [
    path('api/exp/update_info', views.update_data_of_service),
    path('api/exp/add_info', views.add_data_of_service),
]