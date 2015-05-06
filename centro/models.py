from django.db import models

# Create your models here.

class Cursos(models.Model):
	
	Curso = models.CharField(max_length=30)

	def __unicode__(self):
		return self.Curso

	class Meta:
		verbose_name="Curso"
		verbose_name_plural="Cursos"