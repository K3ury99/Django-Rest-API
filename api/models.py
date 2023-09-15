from django.db import models

# Create your models here.


class Libros(models.Model):
    Nombre = models.CharField(max_length=100)
    Fecha_de_registro = models.DateTimeField()
    Autor = models.CharField(max_length=100)
    Precio = models.CharField(max_length=100)
    Editorial = models.CharField(max_length=100)

