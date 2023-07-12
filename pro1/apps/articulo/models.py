from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError 

# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length= 200, null= False)
    activo= models.BooleanField(default=True)
    creacion= models.DateTimeField(auto_now_add= True, null= True)
    actualizacion= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre= models.CharField(max_length= 200, null= False)
    activo= models.BooleanField(default=True)
    creacion= models.DateTimeField(auto_now_add= True)
    actualizacion= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class User(models.Model):
 # Queda por definir como registrar si el usuario es colaborador o publico    
        nombre = models.CharField(max_length= 50, null= False)
        apellido = models.CharField(max_length= 50, null= False)
        telefono = models.CharField(max_length= 20, null= False)
        username = models.CharField(max_length= 10, null= False)
        email = models.EmailField(max_length= 150, unique= True, null= False)
        contrasena = models.CharField(max_length= 8)
        # Se deja para mas adelante las validaciones para el campo contraseña
        fecha_registro = models.DateTimeField(auto_now_add= True)
        avatar = models.ImageField(null=True, blank=True, upload_to='media/user', default='user/default_user.jpg')
        estado = models.BooleanField(default=True)
        online = models.BooleanField(default= False)

        def clean(self):
        # Valida que los datos ingresados sean solo numericos    
            if not self.telefono.isdigit():
                raise ValidationError('Ingrese solo numeros en el campo Telefono')
        
class Articulo(models.Model):
        
    #self.id_usuario = id_usuario
    titulo = models.CharField(max_length= 250, null= False)
    bajada = models.CharField(max_length= 600, null= False, default= 'Sin bajada')
    contenido = models.TextField(null= False)
    fecha_publicacion= models.DateTimeField(auto_now_add= True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media/articulo', default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria= models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True, default= 'Sin Categoria')
    autor=  models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    # Se decide True para Null para permitir el on_delete
    publicado= models.BooleanField(default=False)

    class Meta:
        ordering= ('-publicado', )
        
    def __str__(self):
        return self.titulo
        
    def delete(self, using= None, keep_parents= False):
        self.imagen.delete(self.imagen.name)
        super().delete()


       








       
