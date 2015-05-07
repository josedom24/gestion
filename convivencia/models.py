# -*- coding: utf-8 -*-
from django.db import models
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
		return self.IdAlumnos.Nombre 

	class Meta:
		verbose_name="Amonestación"
		verbose_name_plural="Amonestaciones"