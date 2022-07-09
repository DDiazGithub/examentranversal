from django.urls import path
from .views import home, form_vehiculo, registromascotas, crearcuenta, iniciosesion2, peluqueria, perfil, recuperarcontra, veterinaria, tienda, registrarmascotas, listar_mascotas

urlpatterns = [
    path('', home, name="home"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
    path('registromascotas/', registromascotas, name="registromascotas"),
    path('crearcuenta/', crearcuenta, name="crearcuenta"),
    path('iniciosesion2/', iniciosesion2, name="iniciosesion2"),
    path('peluqueria/', peluqueria, name="peluqueria"),
    path('perfil/', perfil, name="perfil"),
    path('recuperarcontra/', recuperarcontra, name="recuperarcontra"),
    path('veterinaria/', veterinaria, name="veterinaria"),
    path('tienda/', tienda, name="tienda"),
    path('registrarmascotas/', registrarmascotas, name="registrarmascotas"),
    path('listar-mascotas/', listar_mascotas, name="listar_mascotas"),
]