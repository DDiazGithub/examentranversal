from django.contrib import admin
from .models import Categoria, Vehiculo, Mascota

# Register your models here.
#permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Mascota)
