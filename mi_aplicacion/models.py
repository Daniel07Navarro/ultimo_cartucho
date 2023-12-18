from django.db import models

# Create your models here.

class Pais(models.Model):
    idpais = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    poblacion = models.PositiveBigIntegerField()
    estado = models.CharField(max_length=1)