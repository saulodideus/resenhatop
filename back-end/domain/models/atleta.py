from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .racha import *

class Atleta(models.Model):
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=32)
    telefone = models.CharField(max_length=20)
    rachas = models.ManyToManyField(Racha, blank=True, related_name="AtletaToRacha")