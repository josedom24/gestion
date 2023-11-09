from centro.models import Profesores
from django.db import models

# Create your models here.
class Correos(models.Model):
	
	Fecha = models.DateField()
	Asunto = models.CharField(max_length=100, blank=True)
	Destinatarios=models.ManyToManyField(Profesores, verbose_name="Destinatarios", blank=True)
	Contenido=models.TextField(blank=True)

	def __str__(self):
		return str(self.Fecha)+self.Asunto

	class Meta:
		verbose_name="Correos"
		verbose_name_plural="Correos"
