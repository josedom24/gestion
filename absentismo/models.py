# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from centro.models import Alumnos

# Create your models here.
class TiposActuaciones(models.Model):
    TipoActuacion = models.CharField(max_length=60)

    def __unicode__(self):
        return self.TipoActuacion

    class Meta:
        verbose_name = "Tipo Actuación"
        verbose_name_plural = "Tipos de Actuación"

class Actuaciones(models.Model):
    medios = (
        ('1', 'Teléfono'),
        ('2', 'Correo ordinario'),
        ('3', 'Correo certificado'),
    )
    IdAlumno = models.ForeignKey(Alumnos)
    Fecha = models.DateField()
    NroFaltas = models.IntegerField(default=0)
    Tipo = models.ForeignKey(TiposActuaciones, related_name='Tipo_de', blank=True, null=True, on_delete=models.SET_NULL)
    Notificada = models.BooleanField()
    Medio = models.CharField(max_length=1, choices=medios, default='1')
    Comentario = models.TextField(blank=True)

    def __unicode__(self):
        return self.IdAlumno.Nombre

    class Meta:
        verbose_name = "Actuación"
        verbose_name_plural = "Actuaciones"