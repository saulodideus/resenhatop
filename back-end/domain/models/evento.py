from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .racha import *
from .atleta import *

class Evento(models.Model):
    dataHora = models.DateField()
    descricao = models.CharField(max_length=800)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    racha = models.ManyToOneField(Racha)
    atletas = models.ManyToManyField(Atleta,blank=True, related_name="AtletaToEvento")