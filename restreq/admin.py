from django.contrib import admin

from .models import Autor, Articulo

# Register your models here.

admin.site.register(Autor)
admin.site.register(Articulo)