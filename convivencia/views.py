# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from convivencia.forms import AmonestacionForm,SancionForm,TipoResumen,CitacionForm
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Sanciones,Citaciones
import time,calendar
from datetime import datetime
# Create your views here.
from django.contrib.auth.decorators import login_required
from funciones import funciones
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
def citacion(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	if request.method=='POST':
		form = CitacionForm(request.POST)
		error=True
		if form.is_valid():
			form.save()
			return redirect('/centro/')
	else:
		form = CitacionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%Y")})
		error=False
	context={'alum':alum,'form':form,'error':error}
	return render(request, 'convivencia/citacion.html',context)

@login_required(login_url='/admin/login/')
def historial(request,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	amon=Amonestaciones.objects.filter(IdAlumno_id=alum_id).order_by('Fecha')
	sanc=Sanciones.objects.filter(IdAlumno_id=alum_id).order_by("Fecha")
	cit=Citaciones.objects.filter(IdAlumno_id=alum_id).order_by("Fecha")
	historial=list(amon)+list(sanc)+list(cit)
	historial=sorted(historial, key=lambda x: x.Fecha, reverse=False)
	tipo=[]
	for h in historial:
		tipo.append(str(type(h)).split(".")[2][0])
	hist=zip(historial,tipo,range(1,len(historial)+1))
	context={'alum':alum,'historial':hist}
	return render(request, 'convivencia/historial.html',context)

@login_required(login_url='/admin/login/')
def resumen_hoy(request,tipo):
	hoy=datetime.now()
	return resumen(request,str(hoy.month),str(hoy.year),tipo)


@login_required(login_url='/admin/login/')
def resumen(request,mes,ano,tipo):
	if request.method=='POST':
		tipo=request.POST.get('tipo')

	c = calendar.HTMLCalendar(calendar.MONDAY)
	calhtml=c.formatmonth(int(ano),int(mes))

	if tipo=="a":
		datos=Amonestaciones.objects.filter(Fecha__year=ano).filter(Fecha__month=mes)
	if tipo=="s":
		datos=Sanciones.objects.filter(Fecha__year=ano).filter(Fecha__month=mes)
	if tipo=="c":
		datos=Citaciones.objects.filter(Fecha__year=ano).filter(Fecha__month=mes)

	ult_dia=calendar.monthrange(int(ano),int(mes))[1]
	dic_fechas=datos.values("Fecha")
	fechas=[]
	for f in dic_fechas:
		fechas.append(f["Fecha"])

	for dia in xrange(1,int(ult_dia)+1):
		fecha=datetime(int(ano),int(mes),dia)
		if fecha.date() in fechas:
			calhtml=calhtml.replace(str(dia),'<a href="/convivencia/show/%s/%s/%s/%s"><strong>%s</strong></a>'%(tipo,mes,ano,dia,dia))

	form=TipoResumen(initial={'tipo':tipo})
	
	
	mes_actual=datetime(int(ano),int(mes),1)
	mes_ant=funciones.AddMonths(mes_actual,-1)
	mes_prox=funciones.AddMonths(mes_actual,1)

	context={'calhtml':calhtml,'fechas':[mes_actual,mes_ant,mes_prox],'form':form,'tipo':tipo}
	return render(request, 'convivencia/resumen.html',context)




@login_required(login_url='/admin/login/')
def show(request,dia,mes,ano,tipo):
	fecha=datetime(int(ano),int(mes),int(dia))
	if tipo=="a":
		datos=Amonestaciones.objects.filter(Fecha=fecha)
	if tipo=="s":
		datos=Sanciones.objects.filter(Fecha=fecha)
	if tipo=="c":
		datos=Citaciones.objects.filter(Fecha=fecha)
	datos=zip(range(1,len(datos)+1),datos,funciones.ContarFaltas(datos.values("IdAlumno")))
	context={'datos':datos,'tipo':tipo,'fecha':fecha}
	return render(request, 'convivencia/show.html',context)
