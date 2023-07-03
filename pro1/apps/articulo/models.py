from typing import Any, Dict, Tuple
from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    #self.id = id
    #self.id_usuario = id_usuario
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo',default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null=True, default='Sin categoria')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
        
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        









    #def publicar(self):
        #if  self.online == True:
         #   id = int(input("Ingrese el ID del articulo: "))
          #  titulo = input("Ingrese el título del artículo: ")
           # resumen = input("Ingrese el resumen del artículo: ")
            #contenido = input("Ingrese el contenido del artículo: ")
            #imagen = input("Ingrese la URL de la imagen del artículo (opcional): ")
            #estado = "Activo"
            #Articulo(id, self.id, titulo, resumen, contenido, datetime.now(), imagen, estado)
        #else:
         #   print("Para poder publicar debe loguearse.")