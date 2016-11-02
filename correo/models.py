from __future__ import unicode_literals
from centro.models import Profesores
from django.db import models

# Create your models here.
class Correos(models.Model):
	
	Fecha = models.DateField()
	Asunto = models.CharField(max_length=100)
	Contenido=models.TextField(blank=True)
	Destinatarios=models.ManyToManyField(Profesores, verbose_name="Destinatarios")

	def __unicode__(self):
		return str(self.Fecha)+self.Asunto

	class Meta:
		verbose_name="Correos"
		verbose_name_plural="Correos"