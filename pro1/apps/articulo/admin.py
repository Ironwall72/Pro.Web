from django.contrib import admin
from .models import Articulo, Categoria, Etiqueta, User

# Register your models here.

@admin.register(Articulo)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'bajada', 'contenido', 'autor', 'fecha_publicacion', 'imagen', 'estado', 'categoria', 'publicado')


class AuthorAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'activo', 'creacion','actualizacion')


admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(User)