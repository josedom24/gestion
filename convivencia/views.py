# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from convivencia.forms import AmonestacionForm,SancionForm
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Sanciones
import time,calendar
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/login/')
def amonestacion(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	if request.method=='POST':
		form = AmonestacionForm(request.POST)
		error=True
		if form.is_valid():
			form.save()
			return redirect('/centro/')
	else:
		form = AmonestacionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%Y")})
		error=False
	context={'alum':alum,'form':form,'error':error}
	return render(request, 'convivencia/amonestacion.html',context)

@login_required(login_url='/admin/login/')
def sancion(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	if request.method=='POST':
		form = SancionForm(request.POST)
		error=True
		if form.is_valid():
			form.save()
			return redirect('/centro/')
	else:
		form = SancionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%Y")})
		error=False
	context={'alum':alum,'form':form,'error':error}
	return render(request, 'convivencia/sancion.html',context)

@login_required(login_url='/admin/login/')
def historial(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	amon=Amonestaciones.objects.filter(IdAlumno_id=alum_id).order_by('Fecha')
	sanc=Sanciones.objects.filter(IdAlumno_id=alum_id).order_by("Fecha")
	historial=list(amon)+list(sanc)
	historial=sorted(historial, key=lambda x: x.Fecha, reverse=False)
	tipo=[]
	for h in historial:
		tipo.append(str(type(h)).split(".")[2][0])
	hist=zip(historial,tipo,range(1,len(historial)+1))
	context={'alum':alum,'historial':hist}
	return render(request, 'convivencia/historial.html',context)

@login_required(login_url='/admin/login/')
def historial(request,mes,ano):
	c = calendar.HTMLCalendar(calendar.MONDAY)
	calhtml=c.formatmonth(int(ano),int(mes))
	fecha=[mes,ano]
	context={'caltml':caltml,"fecha":fecha}
	return render(request, 'convivencia/resumen.html',context)


