from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


def centro(request):
    return render(request,'centro.html')

def registro(request):
    return render(request,'registro.html')

def inicio(request):
    return render(request,'inicio.html')

def login (request):
    return render(request,'login.html')

def about (request):
    return render(request,'about.html')

def tienda (request):
    return render(request,'tienda.html')

def contacto(request):
    return render(request,'contacto.html')

def single(request):
    return render(request,'single.html')

def centro(request):
    return render(request,'carro.html')

def sucursal(request):
    return render(request,'sucursal.html')


def clientelista(request):
    return render(request,'clientelista.html')
#def loginADM(request):
 #   return render(request,'loginADM.html')
def adm_home(request):
    return render(request,'homeADM.html')

def loginADM(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admHome')  # Asegúrate de que 'admHome' esté definido en tus URLs
        else:
            # Mensaje de error de inicio de sesión no válido
            return render(request, 'backen.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'backen.html')

def adm_home(request):
    return render(request, 'homeADM.html')

def tablaLibro(request):
    return render(request, 'nuevoLibro.html')




def insitucion(request):
    return render(request, 'institution.html')


def master(request):
    return render(request, 'master.html')

def base(request):
    return render(request, 'base.html')

def tablaClienteListar(request):
    return render(request, 'TablaCliente.html')


def modificacion(request):
    return render(request, 'modifi.html')


def sucursarAgregar(request):
    return render(request, 'AddSucurs.html')

def modifiSucursal(request):
    return render(request, 'ModiSucurs.html')

def listarLibro(request):
    return render(request, 'listarLibro.html')


def catalogoLibro(request):
    return render(request, 'catLogo.html')


def pago(request):
    return render(request, 'pago.html')

def registroPago(request):
    return render(request, 'RegisPago.html')


def galeria(request):
    return render(request, 'galeria.html')


def login_new(request):
    return render(request, 'login_new.html')

