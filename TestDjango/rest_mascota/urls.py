from django.urls import path
from rest_mascota.views import api_mascotas, info_mascotas

urlpatterns = [
    path('api_mascotas', api_mascotas, name="api_mascotas"),
    path('info_mascotas/<id>', info_mascotas, name="info_mascotas"),
]