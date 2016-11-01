from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Procedencia(models.Model):
	Procedencia=models.CharField(max_length=30)

	def __unicode__(self):
		return self.Procedencia

	class Meta:
		verbose_name="Procedencia"
		verbose_name_plural="Procedencias"

class Remitente(models.Model):
	Remitente=models.CharField(max_length=40)

	def __unicode__(self):
		return self.Remitente

	class Meta:
		verbose_name="Remitente"
		verbose_name_plural="Remitentes"

class ClaseDocumento(models.Model):
	ClaseDocumento=models.CharField(max_length=20)

	def __unicode__(self):
		return self.ClaseDocumento

	class Meta:
		verbose_name="Documento"
		verbose_name_plural="Documentos"

class Registro(models.Model):
	Curso = models.CharField(max_length=9)
	Fecha = models.DateField()
	N=models.IntegerField()
	Tipo = models.CharField(max_length=7)
	Idp= models.ForeignKey(Procedencia,null=True,blank=True)
	Idr= models.ForeignKey(Remitente,null=True,blank=True)
	Idc= models.ForeignKey(ClaseDocumento,null=True,blank=True)
	Contenido=models.TextField(blank=True)

	def __unicode__(self):
		return self.Curso+' - ' + str(self.N)+' - ' + str(self.Fecha)+ ' - '+self.Tipo +' - '+self.Contenido

	class Meta:
		verbose_name="Registro"
		verbose_name_plural="Registros"
