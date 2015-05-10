# -*- coding: utf-8 -*-
from django.shortcuts import render
from convivencia.forms import AmonestacionForm
from centro.models import Alumnos
import time
# Create your views here.

def amonestacion(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	form = AmonestacionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%y")})
	context={'alum':alum,'form':form}
	return render(request, 'convivencia/amonestacion.html',context)