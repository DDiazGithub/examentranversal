from django.urls import path
from rest_mascota.views import api_mascotas

urlpatterns = [
    path('api_mascotas', api_mascotas, name="api_mascotas"),
]