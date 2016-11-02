# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from centro.models import Alumnos,Profesores

# Register your models here.


class Amonestaciones(models.Model):
	hora = (
		('1','Primera'),
		('2','Segunda'),
		('3','Tercera'),
		('4','Recreo'),
		('5','Cuarta'),
		('6','Quinta'),
		('7','Sexta'),

	)
	IdAlumno = models.ForeignKey(Alumnos)
	Fecha = models.DateField()
	Hora = models.CharField(max_length=1,choices=hora,default='1')
	Comentario=models.TextField(blank=True)
	Profesor = models.ForeignKey(Profesores)
	

	def __unicode__(self):
		return self.IdAlumno.Nombre 

	class Meta:
		verbose_name="Amonestación"
		verbose_name_plural="Amonestaciones"


class Sanciones(models.Model):
	
	IdAlumno = models.ForeignKey(Alumnos)
	Fecha = models.DateField()
	Fecha_fin = models.DateField(verbose_name="Fecha finalización")
	Sancion=models.CharField(max_length=100,blank=True)
	Comentario=models.TextField(blank=True)
	

	def __unicode__(self):
		return self.IdAlumno.Nombre 

	class Meta:
		verbose_name="Sanción"
		verbose_name_plural="Sanciones"