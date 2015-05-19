# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Carta(models.Model):
	Titulo = models.CharField("Título",max_length=30)
	Contenido=models.TextField(blank=True)

	def __unicode__(self):
		return self.Titulo

	class Meta:
		verbose_name="Carta"
		verbose_name_plural="Cartas"