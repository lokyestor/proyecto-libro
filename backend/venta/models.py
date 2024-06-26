
from django.db import models

# Create your models here.
#tiene todo lo necesario por lo que la tabla funciona correctamente
#tabla region

class Region (models.Model):
    
    idRegion = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
    	db_table = 'molina_region'

#tabla provincia
class Provincia(models.Model):
    idProvincia =models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
    	db_table = 'molina_provincia'

#tabla comuna
class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='id_provincia')

    # def __init__(self,id,codigo=None,nombre=None,fCreacion=None,provincia=None):
    #     self.fCreacion = fCreacion
    #     if (provincia != None):
    #         self.provincia=provincia
    #         self.idComuna=id
    #         self.codigo=codigo
    #         self.nombre=nombre

    def __str__(self):
        return self.nombre

    class Meta:
    	db_table = 'molina_comuna'


class Direccion(models.Model):
    idDireccion = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'molina_direccion'


#Pais
class Pais(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'molina_pais'



class CategoriaLibro(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    categoria  = models.CharField(max_length=100)
    # Otros campos según sea necesario



    def __str__(self):
        return self.categoria

    class Meta:
        db_table = 'molina_categoria'

#Editorial
class Editorial(models.Model):
    idEditorial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'molina_ditorial'


class GeneroLibro(models.Model):
    idGenero = models.IntegerField(primary_key=True)
    genero = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genero

    class Meta:
        db_table = 'molina_genero_libro'


class Idioma(models.Model):
    idIdioma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'molina_idioma'

        



#tabla tapa libro        
class TapaLibro(models.Model):
    idTapaLibro = models.IntegerField(primary_key=True)
    tapaLibro = models.CharField(max_length=100)

    def __str__(self):
        return self.tapaLibro

    class Meta:
        db_table = 'molina_tapa_libro'


#tabla origen libro
class OrigenLibro(models.Model):
    idOrigen = models.IntegerField(primary_key=True)
    origenLibro = models.CharField(max_length=100)
    def __str__(self):
        return self.origenLibro

    class Meta:
        db_table = 'molina_origen_libro'


class EstadoLibro(models.Model):
    idEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.estado 

    class Meta:
        db_table = 'molina_estado_libro'
#tabla libro

class Libro(models.Model):
    idLibro = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=200,unique=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='id_editorial')
    categoria = models.ForeignKey(CategoriaLibro, on_delete=models.CASCADE, db_column='id_categoria')
    genero = models.ForeignKey(GeneroLibro, on_delete=models.CASCADE, db_column='id_genero')
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, db_column='id_idioma')
    tapa = models.ForeignKey(TapaLibro, on_delete=models.CASCADE, db_column='id_tapa')
    origen = models.ForeignKey(OrigenLibro, on_delete=models.CASCADE, db_column='id_origen')
    estado = models.ForeignKey(EstadoLibro, on_delete=models.CASCADE, db_column='id_estado')  # Nuevo o usado
   
        

    def __str__(self):
        return self.titulo
    
    class Meta:
    	db_table = 'libro_molina'

#tabla resena libro
class Resena(models.Model):
    idResena = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='id_libro')
    calificacion = models.IntegerField()
    comentario = models.TextField(max_length=1000)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.libro)

    class Meta:
        db_table = 'molina_resena'

#tabla libro editorial
class LibroEditorial(models.Model):
    id = models.IntegerField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    stock = models.IntegerField()
    

    def __str__(self):
        return self.libro

    class Meta:
        db_table = 'molina_libro_editorial'


class GeneroPersona(models.Model):
    idGenero  = models.AutoField( primary_key=True,db_column='id_genero')
    nombre     = models.CharField(max_length=20, blank=False, null=False,db_column='genero')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    

    def __str__(self):
        return self.nombre
    
    class Meta:
    	db_table = 'harrys_genero'
    

class Persona(models.Model):
    rut    = models.IntegerField( primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    papellido = models.CharField(max_length=30, blank=True, null=True)
    sapellido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=False)
    fechaNacimiento = models.DateField(blank=True, null=True, db_column='fecha_nacimiento')
    pais=models.ForeignKey(Pais,models.DO_NOTHING, db_column='id_pais')
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    genero        = models.ForeignKey(GeneroPersona, models.DO_NOTHING, db_column='id_genero')
    

    def __str__(self):
        return str(self.rut)+", "+ self.nombre + ", "+str(self.activo)
    
    class Meta:
    	db_table = 'molina_persona'



class Cliente(models.Model):    
    rut    = models.OneToOneField(Persona, models.DO_NOTHING, primary_key=True,db_column='rut')
    descuento = models.IntegerField(blank=True, null=True,default=0)  

    def __str__(self):
        return self.rut

    class Meta:
    	db_table = 'molina_cliente'




class Cargo(models.Model): 
    idCargo = models.IntegerField(null=False, primary_key=True, db_column='codCargo')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'harrys_cargo'

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)  
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    codCargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    sueldo = models.IntegerField(null=False)
    
    
    def __str__(self):
        return self.rut
    
    class Meta:
    	db_table = 'molina_empleado'



class Nacionalidad(models.Model):
    idNacionalidad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    class Meta:
    	db_table = 'molina_nacionalidad'
    



class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True) 
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    Nacionalidad = models.ForeignKey(Nacionalidad, models.DO_NOTHING, db_column='id_nacionalidad')

    def __str__(self):
        return str(self.rut)
    
    class Meta:
    	db_table = 'molina_autor'





class Sucursal(models.Model):
    idSucursal =models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre=models.CharField(max_length=100,  null=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,default=0, db_column='id_comuna',null=True)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')
    fCreacion =  models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.nombre

    class Meta:
    	db_table = 'harrys_sucursal'



class FormaPago(models.Model): 
    idFPago = models.IntegerField(null=False, primary_key=True,db_column='codFormaPago')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200, null=False,db_column='descripcion')
    
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'molina_formapago'



class Boleta(models.Model):
    idBoleta = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return self.fecha
    class Meta:
    	db_table = 'molina_boleta'



class DetalleBoleta(models.Model):
    idDetalleBoleta = models.IntegerField(primary_key=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, db_column='id_boleta')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='id_libro')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)




    def __str__(self):
        return self.boleta
    class Meta:
    	db_table = 'molina_detalle_boleta'
