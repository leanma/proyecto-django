from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)
