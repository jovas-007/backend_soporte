from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication

class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"


class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Perfil de {self.user.first_name} {self.user.last_name}"

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    base_ki = models.FloatField()
    total_ki = models.FloatField()
    afiliacion = models.CharField(max_length=100)

     # NUEVO
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="personajes/", blank=True, null=True)
    imagen_url = models.URLField(blank=True)
    def __str__(self):
        return self.nombre
