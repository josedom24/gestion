# -*- coding: utf-8 -*-
from django.db import models
from centro.models import Alumnos,Profesores

# Register your models here.

class FaltasLeves(models.Model):
	Falta = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.Falta

	class Meta:
		verbose_name="Falta Leve"
		verbose_name_plural="Faltas Leves"

class FaltasGraves(models.Model):
	Falta = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.Falta

	class Meta:
		verbose_name="Falta Grave"
		verbose_name_plural="Faltas Graves"


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
	FaltasLeves = models.ManyToManyField(FaltasLeves,verbose_name="Faltas Leves",blank=True)
	FaltasGraves = models.ManyToManyField(FaltasGraves,verbose_name="Faltas Graves",blank=True)

	def __unicode__(self):
		return self.IdAlumno.Nombre 

	class Meta:
		verbose_name="Amonestación"
		verbose_name_plural="Amonestaciones"


class SancionesLeves(models.Model):
	Sancion = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.Sancion

	class Meta:
		verbose_name="Sanción Leve"
		verbose_name_plural="Sanciones Leves"

class SancionesGraves(models.Model):
	Sancion = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.Sancion

	class Meta:
		verbose_name="Sanción Grave"
		verbose_name_plural="Sanciones Graves"

class SancionesOtras(models.Model):
	Sancion = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.Sancion

	class Meta:
		verbose_name="Otra Sanción"
		verbose_name_plural="Otras Sanciones"



class Sanciones(models.Model):
	
	IdAlumno = models.ForeignKey(Alumnos)
	Fecha = models.DateField()
	Fecha_fin = models.DateField(verbose_name="Fecha finalización")
	Comentario=models.TextField(blank=True)
	
	SancionesLeves = models.ManyToManyField(SancionesLeves,verbose_name="Sanciones Leves",blank=True)
	SancionesGraves = models.ManyToManyField(SancionesGraves,verbose_name="Sanciones Graves",blank=True)
	SancionesOtras= models.ManyToManyField(SancionesOtras,verbose_name="Otras Sanciones",blank=True)

	def __unicode__(self):
		return self.IdAlumno.Nombre 

	class Meta:
		verbose_name="Sanción"
		verbose_name_plural="Sanciones"
