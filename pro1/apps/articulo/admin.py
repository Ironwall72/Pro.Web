from django.contrib import admin
from .models import Articulo,Categoria

# Register your models here.

@admin.register(Articulo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','resumen','contenido','fecha_publicacion','imagen','estado','categoria','publicado')
