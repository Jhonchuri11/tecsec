from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    numero = models.CharField(max_length=9)
    password = models.CharField(max_length=255, unique=True)

    REQUIRED_FIELDS = ['email']

class Calle(models.Model):
    nombre = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    nivel_seguridad = models.IntegerField()


class Comentario(models.Model):
    id_calle = models.ForeignKey(Calle, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Incidente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

class CallePeligrosa(models.Model):
    id_calle = models.ForeignKey(Calle, on_delete=models.CASCADE)
    nivel_peligro = models.IntegerField()


class Cliente(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, unique=True)

    


    