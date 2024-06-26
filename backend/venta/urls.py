
from django.contrib import admin
from django.urls import path
from venta import views
from .views import PersonaList, PersonaDetail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    
    path('apix/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apix/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('region/', views.RegionList.as_view(), name='region-list'),
    path('region/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),


    path('provincia/', views.ProvinciaList.as_view(), name='provincia-list'),
    path('provincia/<int:pk>/', views.ProvinciaDetail.as_view(), name='provincia-detail'),


    path('comuna/', views.ComunaList.as_view(), name='comuna-list'),
    path('comuna/<int:pk>/', views.ComunaDetail.as_view(), name='comuna-detail'),


    path('idioma/', views.IdiomaList.as_view(), name='idioma-list'),
    path('idioma/<int:pk>/', views.IdiomaDetail.as_view(), name='idioma-detail'),


    path('editorial/', views.EditorialList.as_view(), name='editorial-list'),
    path('editorial/<int:pk>/', views.EditorialDetail.as_view(), name='editorial-detail'),


    path('libro/', views.LibroList.as_view(), name='libro-list'),
    path('libro/<int:pk>/', views.LibroDetail.as_view(), name='libro-detail'),


    path('resena/', views.ResenaList.as_view(), name='resena-list'),
    path('resena/<int:pk>/', views.ResenaDetail.as_view(), name='resena-detail'),


    path('pais/', views.PaisList.as_view(), name='pais-list'),
    path('pais/<int:pk>/', views.PaisDetail.as_view(), name='pais-detail'),


    path('estado/', views.EstadoLibroList.as_view(), name='estado-list'),    
    path('estado/<int:pk>/', views.EstadoLibroDetail.as_view(), name='estado-detail'),


    path('personas/', PersonaList.as_view(), name='persona-list'),    
    path('personas/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),


    path('pais/', views.PaisList.as_view(), name='pais-list'),
    path('pais/<int:pk>/', views.PaisDetail.as_view(), name='pais-detail'),


    path('api/genero_persona/', views.GeneroPersonaList.as_view(), name='genero_persona-list'),
    path('api/genero_persona/<int:pk>/', views.GeneroPersonaDetail.as_view(), name='genero_persona-detail'),


    path('direcciones/', views.DireccionList.as_view(), name='direccion-list'),
    path('direcciones/<int:pk>/', views.DireccionDetail.as_view(), name='direccion-detail'),


    path('tapas/', views.TapaLibroList.as_view(), name='tapalibro-list'),
    path('tapas/<int:pk>/', views.TapaLibroDetail.as_view(), name='tapalibro-detail'),


    path('categorias/', views.CategoriaLibroList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaLibroDetail.as_view(), name='categoria-detail'),


    path('generos/', views.GeneroLibroList.as_view(), name='genero-list'),
    path('generos/<int:pk>/', views.GeneroLibroDetail.as_view(), name='genero-detail'),


    path('libroeditorial/', views.LibroEditorialList.as_view(), name='libroeditorial-list'),
    path('libroeditorial/<int:pk>/', views.LibroEditorialDetail.as_view(), name='libroeditorial-detail'),


    path('cliente/', views.ClienteList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),


    path('cargo/', views.CargoList.as_view(), name='cargo-list'),
    path('cargo/<int:pk>/', views.CargoDetail.as_view(), name='cargo-detail'),


    path('empleado/', views.EmpleadoList.as_view(), name='empleado-list'),
    path('empleado/<int:pk>/', views.EmpleadoDetail.as_view(), name='empleado-detail'),

    path('nacionalidad/', views.NacionalidadList.as_view(), name='nacionalidad-list'),
    path('nacionalidad/<int:pk>/', views.NacionalidadDetail.as_view(), name='nacionalidad-detail'),


    path('nacionalidad/', views.NacionalidadList.as_view(), name='nacionalidad-list'),
    path('nacionalidad/<int:pk>/', views.NacionalidadDetail.as_view(), name='nacionalidad-detail'),


    path('autor/', views.AutorList.as_view(), name='autor-list'),
    path('autor/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),


    path('sucursal/', views.SucursalList.as_view(), name='sucursal-list'),
    path('sucursal/<int:pk>/', views.SucursalDetail.as_view(), name='sucursal-detail'),


    path('formapago/', views.FormaPagoList.as_view(), name='formapago-list'),
    path('formapago/<int:pk>/', views.FormaPagoDetail.as_view(), name='formapago-detail'),

    path('boleta/', views.BoletaList.as_view(), name='boleta-list'),
    path('boleta/<int:pk>/', views.BoletaDetail.as_view(), name='boleta-detail'),


    path('detalle-boleta/', views.DetalleBoletaList.as_view(), name='detalle-boleta-list'),
    path('detalle-boleta/<int:pk>/', views.DetalleBoletaDetail.as_view(), name='detalle-boleta-detail'),

    path('origenes/', views.OrigenLibroList.as_view(), name='origenlibro-list'),
    path('origenes/<int:pk>/', views.OrigenLibroDetail.as_view(), name='origenlibro-detail'),

    path('venta/confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    
    path('libros/',  views.LibroList.as_view()),
    path('libros_login/',  views.LibroListLogin.as_view()),
]
