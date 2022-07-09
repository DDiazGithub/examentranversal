from django import forms
from django.forms import ModelForm
from .models import Vehiculo, Mascota

# creamos clase para el formulario desde la base de datos
class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo 
        fields =['patente','marca','modelo','categoria']

class MascotaForm(ModelForm):

    class Meta:
        model = Mascota
        fields = '__all__'