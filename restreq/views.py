from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ArticuloSerializer, AutorSerializer
from .models import Autor, Articulo

# Create your views here.

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer
    
class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().order_by('titulo')
    serializer_class = ArticuloSerializer