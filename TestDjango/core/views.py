from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForm, MascotaForm

# Create your views here.

def home(request):
    #acceddiendo al objeto que tiene los datos de la base
    # el metodo que traera todos los vehiculos all
    vehiculos= Vehiculo.objects.all()
    # ahoras crearemos una variable que le pase los datos del vehiculo a la template
    datos = {
        'vehiculos': vehiculos
    }

    return render(request, 'core/home.html', datos)

def form_vehiculo(request):
    return render(request, 'core/form_vehiculo.html')

def registromascotas(request):
    return render(request, 'core/registromascotas.html')
def crearcuenta(request):
    return render (request, 'core/crearcuenta.html')
def iniciosesion2(request):
    return render (request, 'core/iniciosesion2.html')
def peluqueria(request):
    return render (request, 'core/peluqueria.html')
def perfil(request):
    return render (request, 'core/perfil.html')
def recuperarcontra(request):
    return render (request, 'core/recuperarcontra.html')
def veterinaria(request):
    return render (request, 'core/veterinaria.html')
def tienda(request):
    return render (request, 'core/tienda.html')
def registrarmascotas(request):
    data = {
        'form': MascotaForm()
    }
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mascota guardada"
        else:
            data["form"] = formulario
    return render (request, 'core/registrarmascotas.html',data)

def listar_mascotas(request):


    return render(request, 'core/listar_mascotas.html')
