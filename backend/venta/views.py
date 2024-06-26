from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class LibroListLogin(APIView):
    # Todo lo que este dentro de la clase Exige el Token 
    # debe venir con Bearer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
         registro = Libro.objects.all()
         serializer = LibroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class LibroList(APIView):
    def get(self, request, format=None):
         registro = Libro.objects.all()
         serializer = LibroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")    
     
     
     
     

class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)

#fin del JSONResponseOkRows, JSONResponseOk, JSONResponseErr
    
#tablas de base de datos

#tabla definicion region esta lista

def region(request):
    registro = Region.objects.all()
    print("Registro",registro)
    serializer=RegionSerializer(registro, many=True)
    # return HttpResponse("hola")
    return JSONResponseOkRows(serializer.data,"")

class RegionList(APIView):
    def get(self, request, format=None):
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = RegionSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class RegionDetail(APIView):
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

    def get(self, request, format=None):
         registro = Libro.objects.all()
         serializer = LibroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = RegionSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    #revisar a detalle las class de libro


    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404
        
        
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = RegionSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = RegionSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

#----------------------------------    
#falta agregar class provinciaList(APIView)
#falta agregar class provinciaDetail(APIView)
# Vistas para Provincia
def provincia(request):
    registro = Provincia.objects.all()
    print("Registro", registro)
    serializer = ProvinciaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ProvinciaList(APIView):
    def get(self, request, format=None):
        registro = Provincia.objects.all()
        serializer = ProvinciaSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ProvinciaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class ProvinciaDetail(APIView):
    def get_object(self, pk):
        try:
            return Provincia.objects.get(pk=pk)
        except Provincia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = ProvinciaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = ProvinciaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Comuna
def comuna(request):
    registro = Comuna.objects.all()
    print("Registro", registro)
    serializer = ComunaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ComunaList(APIView):
    def get(self, request, format=None):
        registro = Comuna.objects.all()
        serializer = ComunaSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ComunaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class ComunaDetail(APIView):
    def get_object(self, pk):
        try:
            return Comuna.objects.get(pk=pk)
        except Comuna.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = ComunaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = ComunaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Idioma
def idioma(request):
    registro = Idioma.objects.all()
    print("Registro", registro)
    serializer = IdiomaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class IdiomaList(APIView):
    def get(self, request, format=None):
        registro = Idioma.objects.all()
        serializer = IdiomaSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = IdiomaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class IdiomaDetail(APIView):
    def get_object(self, pk):
        try:
            return Idioma.objects.get(pk=pk)
        except Idioma.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = IdiomaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = IdiomaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Editorial
def editorial(request):
    registro = Editorial.objects.all()
    print("Registro", registro)
    serializer = EditorialSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class EditorialList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        registro = Editorial.objects.all()
        serializer = EditorialSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = EditorialSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class EditorialDetail(APIView):
    def get_object(self, pk):
        try:
            return Editorial.objects.get(pk=pk)
        except Editorial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = EditorialSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = EditorialSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Libro
def libro(request):
    registro = Libro.objects.all()
    print("Registro", registro)
    serializer = LibroSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class LibroList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibroDetail(APIView):
    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        libro = self.get_object(pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Vistas para Resena
def resena(request):
    registro = Resena.objects.all()
    print("Registro", registro)
    serializer = ResenaSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ResenaList(APIView):
    def get(self, request, format=None):
        registro = Resena.objects.all()
        serializer = ResenaSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ResenaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class ResenaDetail(APIView):
    def get_object(self, pk):
        try:
            return Resena.objects.get(pk=pk)
        except Resena.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = ResenaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = ResenaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Pais
def pais(request):
    registro = Pais.objects.all()
    print("Registro", registro)
    serializer = PaisSerializer(registro, many=True)
    return JSONResponseOkRows(serializer.data, "")

class PaisList(APIView):
    def get(self, request, format=None):
        registro = Pais.objects.all()
        serializer = PaisSerializer(registro, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = PaisSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED, msg="")
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class PaisDetail(APIView):
    def get_object(self, pk):
        try:
            return Pais.objects.get(pk=pk)
        except Pais.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = PaisSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = PaisSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponseOk(None, msg="Registro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#creacion de la pagina backend definir atributo y llamar a la carpeta html
def login(request):
    return render(request,'login.html')

def home(request):
    if request.method == 'POST':
        # Lógica para manejar la solicitud POST del formulario de inicio de sesión
        # Aquí puedes realizar la autenticación del usuario y redirigirlo a la página de inicio
        return render(request, 'home.html')
    else:
        # Lógica para mostrar la página de inicio si la solicitud no es POST
        return render(request, 'home.html')
    
def cliente(request):
    return render(request,'cliente.html')

def listacliente(request):
    return render(request,'clientelista.html')

def test(request):
    return render(request,'test.html')
#--------------------------------------



def estado(request):
    registro = EstadoLibro.objects.all()
    print("Registro",registro)
    serializer=EstadoLibroSerializer(registro, many=True)
    # return HttpResponse("hola")
    return JSONResponseOkRows(serializer.data,"")

class EstadoLibroList(APIView):
    def get(self, request, format=None):
        estados = EstadoLibro.objects.all()
        serializer = EstadoLibroSerializer(estados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoLibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstadoLibroDetail(APIView):
    def get_object(self, pk):
        try:
            return EstadoLibro.objects.get(pk=pk)
        except EstadoLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        estado = self.get_object(pk)
        serializer = EstadoLibroSerializer(estado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        estado = self.get_object(pk)
        serializer = EstadoLibroSerializer(estado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        estado = self.get_object(pk)
        estado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_object(self, pk):
        try:
            return EstadoLibro.objects.get(pk=pk)
        except EstadoLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = EstadoLibroSerializer(registro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = EstadoLibroSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_object(self, pk):
        try:
            return EstadoLibro.objects.get(pk=pk)
        except EstadoLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = EstadoLibroSerializer(registro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        registro = self.get_object(pk)
        serializer = EstadoLibroSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def persona(request):
    registro = Persona.objects.all()
    serializer = PersonaSerializer(registro, many=True)
    return JsonResponse(serializer.data,"")

class PersonaList(APIView):
    def get(self, request, format=None):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def generoPersona(request):
    registros = GeneroPersona.objects.all()
    serializer = GeneroPersonaSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class GeneroPersonaList(APIView):
    def get(self, request, format=None):
        generos = GeneroPersona.objects.all()
        serializer = GeneroPersonaSerializer(generos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroPersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#primeta parte 
class GeneroPersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return GeneroPersona.objects.get(pk=pk)
        except GeneroPersona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroPersonaSerializer(genero)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroPersonaSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genero = self.get_object(pk)
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def direccion(request):
    registros = Direccion.objects.all()
    serializer = DireccionSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class DireccionList(APIView):
    def get(self, request, format=None):
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(direcciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DireccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DireccionDetail(APIView):
    def get_object(self, pk):
        try:
            return Direccion.objects.get(pk=pk)
        except Direccion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        direccion = self.get_object(pk)
        serializer = DireccionSerializer(direccion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        direccion = self.get_object(pk)
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        direccion = self.get_object(pk)
        direccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def tapaLibro(request):
        registros = TapaLibro.objects.all()
        serializer = TapaLibroSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

class TapaLibroList(APIView):
    def get(self, request, format=None):
        tapas = TapaLibro.objects.all()
        serializer = TapaLibroSerializer(tapas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TapaLibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TapaLibroDetail(APIView):

    def get_object(self, pk):
        try:
            return TapaLibro.objects.get(pk=pk)
        except TapaLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tapa = self.get_object(pk)
        serializer = TapaLibroSerializer(tapa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tapa = self.get_object(pk)
        serializer = TapaLibroSerializer(tapa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tapa = self.get_object(pk)
        tapa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
def categoriaLibro(request):
    registros = CategoriaLibro.objects.all()
    serializer = CategoriaLibroSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class CategoriaLibroList(APIView):
    def get(self, request, format=None):
        registros = CategoriaLibro.objects.all()
        serializer = CategoriaLibroSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

class CategoriaLibroDetail(APIView):
    def get_object(self, pk):
        try:
            return CategoriaLibro.objects.get(pk=pk)
        except CategoriaLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaLibroSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaLibroSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def generoLibro(request):
    registros = GeneroLibro.objects.all()
    serializer = GeneroLibroSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class GeneroLibroList(APIView):
    def get(self, request, format=None):
        generos = GeneroLibro.objects.all()
        serializer = GeneroLibroSerializer(generos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroLibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeneroLibroDetail(APIView):
    def get_object(self, pk):
        try:
            return GeneroLibro.objects.get(pk=pk)
        except GeneroLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroLibroSerializer(genero)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroLibroSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genero = self.get_object(pk)
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def libroEditorial(request):
    registros = LibroEditorial.objects.all()
    serializer = LibroEditorialSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class LibroEditorialList(APIView):
    def get(self, request, format=None):
        libros_editoriales = LibroEditorial.objects.all()
        serializer = LibroEditorialSerializer(libros_editoriales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LibroEditorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibroEditorialDetail(APIView):
    def get_object(self, pk):
        try:
            return LibroEditorial.objects.get(pk=pk)
        except LibroEditorial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        libro_editorial = self.get_object(pk)
        serializer = LibroEditorialSerializer(libro_editorial)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        libro_editorial = self.get_object(pk)
        serializer = LibroEditorialSerializer(libro_editorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        libro_editorial = self.get_object(pk)
        libro_editorial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def cliente(request):
    registros = Cliente.objects.all()
    serializer = ClienteSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class ClienteList(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def cargo(request):
    registros = Cargo.objects.all()
    serializer = CargoSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class CargoList(APIView):
    def get(self, request, format=None):
        cargos = Cargo.objects.all()
        serializer = CargoSerializer(cargos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CargoDetail(APIView):
    def get_object(self, pk):
        try:
            return Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cargo = self.get_object(pk)
        serializer = CargoSerializer(cargo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cargo = self.get_object(pk)
        serializer = CargoSerializer(cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cargo = self.get_object(pk)
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def empleado(request):
    registros = Empleado.objects.all()
    serializer = EmpleadoSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class EmpleadoList(APIView):
    def get(self, request, format=None):
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpleadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empleado = self.get_object(pk)
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        empleado = self.get_object(pk)
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def nacionalidad(request):
    registros = Nacionalidad.objects.all()
    serializer = NacionalidadSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class NacionalidadList(APIView):
    def get(self, request, format=None):
        nacionalidades = Nacionalidad.objects.all()
        serializer = NacionalidadSerializer(nacionalidades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NacionalidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NacionalidadDetail(APIView):

    def get_object(self, pk):
        try:
            return Nacionalidad.objects.get(pk=pk)
        except Nacionalidad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nacionalidad = self.get_object(pk)
        serializer = NacionalidadSerializer(nacionalidad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nacionalidad = self.get_object(pk)
        serializer = NacionalidadSerializer(nacionalidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nacionalidad = self.get_object(pk)
        nacionalidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


def autor(request):
    registros = Autor.objects.all()
    serializer = AutorSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class AutorList(APIView):
    def get(self, request, format=None):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorDetail(APIView):

    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        autor = self.get_object(pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def sucursal(request):
    registros = Sucursal.objects.all()
    serializer = SucursalSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")


class SucursalList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        sucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SucursalDetail(APIView):
    def get_object(self, pk):
        try:
            return Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sucursal = self.get_object(pk)
        serializer = SucursalSerializer(sucursal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sucursal = self.get_object(pk)
        serializer = SucursalSerializer(sucursal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sucursal = self.get_object(pk)
        sucursal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def formaPago(request):
    registros = FormaPago.objects.all()
    serializer = FormaPagoSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class FormaPagoList(APIView):
    def get(self, request, format=None):
        formapagos = FormaPago.objects.all()
        serializer = FormaPagoSerializer(formapagos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FormaPagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormaPagoDetail(APIView):
    def get_object(self, pk):
        try:
            return FormaPago.objects.get(pk=pk)
        except FormaPago.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        formapago = self.get_object(pk)
        serializer = FormaPagoSerializer(formapago)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        formapago = self.get_object(pk)
        serializer = FormaPagoSerializer(formapago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        formapago = self.get_object(pk)
        formapago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def boleta(request):
    registros = Boleta.objects.all()
    serializer = BoletaSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class BoletaList(APIView):
    def get(self, request, format=None):
        boletas = Boleta.objects.all()
        serializer = BoletaSerializer(boletas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoletaDetail(APIView):
    def get_object(self, pk):
        try:
            return Boleta.objects.get(pk=pk)
        except Boleta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        boleta = self.get_object(pk)
        serializer = BoletaSerializer(boleta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        boleta = self.get_object(pk)
        serializer = BoletaSerializer(boleta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        boleta = self.get_object(pk)
        boleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def detalleBoleta(request):
    registros = DetalleBoleta.objects.all()
    serializer = DetalleBoletaSerializer(registros, many=True)
    return JSONResponseOkRows(serializer.data, "")

class DetalleBoletaList(APIView):
    def get(self, request, format=None):
        detalle_boletas = DetalleBoleta.objects.all()
        serializer = DetalleBoletaSerializer(detalle_boletas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DetalleBoletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleBoletaDetail(APIView):
    def get_object(self, pk):
        try:
            return DetalleBoleta.objects.get(pk=pk)
        except DetalleBoleta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detalle_boleta = self.get_object(pk)
        serializer = DetalleBoletaSerializer(detalle_boleta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        detalle_boleta = self.get_object(pk)
        serializer = DetalleBoletaSerializer(detalle_boleta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        detalle_boleta = self.get_object(pk)
        detalle_boleta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OrigenLibroList(APIView):
    def get(self, request, format=None):
        origenes = OrigenLibro.objects.all()
        serializer = OrigenLibroSerializer(origenes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrigenLibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrigenLibroDetail(APIView):
    def get_object(self, pk):
        try:
            return OrigenLibro.objects.get(pk=pk)
        except OrigenLibro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        origen = self.get_object(pk)
        serializer = OrigenLibroSerializer(origen)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        origen = self.get_object(pk)
        serializer = OrigenLibroSerializer(origen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        origen = self.get_object(pk)
        origen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






def detalle_libro(request, libro_id):
    try:
        libro = get_object_or_404(Libro, pk=libro_id)
        # Resto del código para mostrar el detalle del libro
        return render(request, 'detalle_libro.html', {'libro': libro})
    except Libro.DoesNotExist:
        return render(request, 'libro_no_encontrado.html')
    except Exception as e:
        # Manejo genérico de otras excepciones si es necesario
        return render(request, 'error_generico.html', {'error': e})
    

def listar_editoriales(request):
    editoriales = Editorial.objects.all().values('idEditorial', 'nombre')
    data = {
        'OK': True,
        'count': editoriales.count(),
        'registro': list(editoriales),
        'msg': ''
    }
    return JsonResponse(data, safe=False)


def buscar_persona(request):
    query = request.GET.get('query', '')
    if '-' in query:
        rut, dv = query.split('-')
        personas = Persona.objects.filter(rut=rut, dv=dv)
    else:
        personas = Persona.objects.filter(rut=query)
        
    data = list(personas.values())
    return JsonResponse(data, safe=False)


def listar_sucursales(request):
    sucursales = Sucursal.objects.all().values('idSucursal', 'codigo', 'nombre', 'fCreacion', 'comuna__nombre', 'direccion__direccion')
    sucursal_list = list(sucursales)  # Convertir QuerySet a lista
    return JsonResponse(sucursal_list, safe=False)


@csrf_exempt
def confirmar_compra(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        for item in data['items']:
            libro = LibroEditorial.objects.get(id=item['id'])
            libro.stock -= item['cantidad']
            libro.save()
        return JsonResponse({'message': 'Compra confirmada con éxito'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def personas_view(request, rut=None):
    if request.method == 'GET' and 'update' in request.GET:
        if not rut:
            return JsonResponse({'error': 'RUT no proporcionado'}, status=400)
        
        try:
            data = {
                'rut': rut,
                'dv': request.GET.get('dv'),
                'nombre': request.GET.get('nombre'),
                'papellido': request.GET.get('papellido'),
                'sapellido': request.GET.get('sapellido'),
                'email': request.GET.get('email'),
                'fechaNacimiento': request.GET.get('fechaNacimiento'),
                'pais': request.GET.get('pais'),
                'comuna': request.GET.get('comuna'),
                'genero': request.GET.get('genero'),
            }
            persona = Persona.objects.get(rut=rut)
            serializer = PersonaSerializer(persona, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Persona modificada correctamente'})
            else:
                return JsonResponse(serializer.errors, status=400)
        except Persona.DoesNotExist:
            return JsonResponse({'error': 'Persona no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)