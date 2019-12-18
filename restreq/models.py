from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=9999)

    def __str__(self):
        return self.titulo