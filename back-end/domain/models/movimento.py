from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .racha import *
from .atleta import *

class Movimento(models.Model):
    dataHora = models.DateTimeField()
    tipo = models.CharField(max_length=1)
    descricao = models.CharField(max_length=800)
    racha = models.ManyToOneField(Racha)
    atleta = models.ManyToOneField(Atleta,blank=True)
