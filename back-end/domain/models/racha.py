from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from atleta import *
class Racha(models.Model):
    titulo = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    atletas = models.ManyToManyField(Atleta,blank=True, related_name="AtletaToRacha")