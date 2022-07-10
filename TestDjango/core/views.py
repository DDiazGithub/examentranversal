from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Mascota
from .forms import VehiculoForm, MascotaForm #intento

# Create your views here.

def home(request):
    #acceddiendo al objeto que tiene los datos de la base
    # el metodo que traera todos los vehiculos all
    vehiculos= Vehiculo.objects.all()
    # ahoras crearemos una variable que le pase los datos del vehiculo a la template
    datos = {
        'vehiculos': vehiculos
    }                 
   #mascotas= Mascota.objects.all()

   # datos = {
   #     'mascotas': mascotas
   # }

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

    mascotas= Mascota.objects.all()

    data = {
        'mascotas': mascotas
    }


    return render(request, 'core/listar_mascotas.html', data)

def modificarmascotas(request, id):

    mascota = get_object_or_404(Mascota, id=id)

    data = {
        'form': MascotaForm(instance=mascota)
    }

    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_mascotas")
        data ["form"] = formulario


    return render(request, 'core/modificarmascotas.html',data)

def eliminarmascotas(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    return redirect(to="listar_mascotas")