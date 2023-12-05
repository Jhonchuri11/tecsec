from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    numero = models.CharField(max_length=9)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)

    REQUIRED_FIELDS = ['email']

class Cliente(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, unique=True)

    


    