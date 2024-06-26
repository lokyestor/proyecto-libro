
from django.contrib import admin
from django.urls import path
from centro import views
urlpatterns = [
    path('centro/',views.centro),
    path('registro/', views.registro),
    path('home/',views.inicio),
    path('login/',views.login),
    path('nosotros/',views.about),
    path('tienda/',views.tienda),
    path('contacto/', views.contacto),
    path('single/', views.single),
    path('centro/', views.centro),
    #path('loginADM/', views.loginADM),
    path('loginADM/', views.loginADM, name='loginADM'),
    path('admHome/', views.adm_home, name='admHome'),
    path('clientelista/', views.clientelista, name='clientelista'),
    path('tablaLibro/', views.tablaLibro, name='libroLista'),
    path('institucion/', views.insitucion, name= 'institucion'),
    path('master/', views.master, name= 'master'),
    path('base/', views.base, name='base'),
    path('clienteTabla/', views.tablaClienteListar, name='clienteTabla'),
    path('modificarLista/', views.modificacion, name='modificarLista'),
    path('sucursal/', views.sucursal, name='sucursal'),
    path('sucursalAgregar/', views.sucursarAgregar, name='sucursalAgregar'),
    path('sucursalmodificar/', views.modifiSucursal, name='sucursalModificar'),
    path('listarLibro/', views.listarLibro, name='ListarLibro'),
    path('Catalogo/', views.catalogoLibro, name='catalogoLibro'),
    path('compra/', views.pago, name='pago'),
    path('registroPago/', views.registroPago, name='registroPago'),
    path('galeria/', views.galeria, name='galeria'),
    path('login_new/', views.login_new, name='login_new'),
    
    
]
