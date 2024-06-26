from rest_framework import serializers
from .models import *
#llama a la tabla pais de la carpeta models el . es que trae todas las tablas de models
#from .models import Pais

#dato inecesario pero no esta demas revisar los def de la views como get o post

#revisar las clases se modificaron la cantidad de tablas
#posiblemente agregar tablas faltantes de la models con los parametros faltantes
#Faltan definiciones de class
#tabla de libro 3 parametros
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('idRegion', 'codigo', 'nombre')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idProvincia', 'codigo', 'nombre', 'region')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('idComuna', 'codigo', 'nombre', 'provincia')

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('idIdioma', 'nombre')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('idEditorial', 'nombre', 'pais', 'fundacion', 'sitio_web')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('idLibro', 'titulo', 'editorial', 'categoria', 'genero', 'idioma', 'tapa', 'origen', 'estado')
        extra_kwargs = {
            'idLibro': {'read_only': True},  # Make idLibro read-only if it's auto-incremented or not to be provided by the user
            'titulo': {'required': True},
            'editorial': {'required': True},
            'categoria': {'required': True},
            'genero': {'required': True},
            'idioma': {'required': True},
            'tapa': {'required': True},
            'origen': {'required': True},
            'estado': {'required': True},
        }

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('idEditorial', 'nombre')
        extra_kwargs ={
            'idEditorial': {'required': True},
            'nombre': {'required': True},

        }



class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ('idResena', 'libro', 'calificacion', 'comentario', 'fCreacion')

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('idPais', 'nombre')

class EstadoLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoLibro
        fields = ('idEstado', 'nombre')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('rut', 'dv', 'nombre', 'papellido', 'sapellido', 'email', 'fechaNacimiento', 'pais', 'comuna', 'genero')
        extra_kwargs = {
            'fechaNacimiento': {'required': True},
            'dv': {'required': True},
            'email': {'required': True},
            'pais': {'required': True},
            'comuna': {'required': True},
            'genero': {'required': True},
        }
class GeneroPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroPersona
        fields = ['idGenero', 'nombre', 'fCreacion']

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['idGenero', 'nombre']


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['idDireccion', 'direccion']

class TapaLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TapaLibro
        fields = ['idTapaLibro', 'tapaLibro']


class CategoriaLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLibro
        fields = ['idCategoria', 'categoria']


class GeneroLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLibro
        fields = ['idGenero', 'genero']

class LibroEditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroEditorial
        fields = ['id', 'libro', 'precio', 'cantidad', 'stock']



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut', 'descuento']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['idCargo', 'codigo', 'nombre']



class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'rut', 'codCargo', 'sueldo']


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'rut', 'codCargo', 'sueldo']



class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = ['idNacionalidad', 'nombre']



class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['idAutor', 'rut', 'Nacionalidad']


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['idSucursal', 'codigo', 'nombre', 'comuna', 'direccion', 'fCreacion']


class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = ['idFPago', 'codigo', 'nombre']



class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ['idBoleta', 'cliente', 'sucursal', 'forma_pago', 'fecha']



class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBoleta
        fields = ['idDetalleBoleta', 'boleta', 'libro', 'cantidad', 'precio_unitario']


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['idPais', 'nombre']


class EstadoLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoLibro
        fields = ['idEstado', 'estado']


class OrigenLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrigenLibro
        fields = ['idOrigen', 'origenLibro']
        
        


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#https://www.django-rest-framework.org/api-guide/authentication/
#https://coffeebytes.dev/es/django-rest-framework-y-jwt-para-autenticar-usuarios/
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("user:",user)
        token = super().get_token(user)
        print("token:",token)

        # Add custom claims
        token['name'] = user.username
        token['rol'] = "Mauri el Simpatico"
        # ...
        print("token Ultimo:",token)
        return token        