from rest_framework import serializers

from .models import Autor, Articulo

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('pk','nombre', 'email')

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ('pk', 'autores', 'titulo', 'contenido')
