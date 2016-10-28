from django.shortcuts import render,redirect
from convivencia.forms import AmonestacionForm,SancionForm
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Sanciones
from django.contrib.auth.decorators import login_required
import time,calendar

# Create your views here.

@login_required(login_url='/')
def parte(request,tipo,alum_id):
	alum=Alumnos.objects.get(pk=alum_id)
	if request.method=='POST':
		if tipo=="amonestacion":
			form = AmonestacionForm(request.POST)
			titulo="Amonestaciones"
		elif tipo=="sancion":
			form = SancionForm(request.POST)
			titulo="Sanciones"
		else:
			return redirect("/")
		
		if form.is_valid():
			form.save()
			return redirect('/centro/alumnos')
	else:
		if tipo=="amonestacion":
			form = AmonestacionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%Y"),'Hora':1,'Profesor':1})
			
			titulo="Amonestaciones"
		elif tipo=="sancion":
			form = SancionForm({'IdAlumno':alum.id,'Fecha':time.strftime("%d/%m/%Y"),'Fecha_fin':time.strftime("%d/%m/%Y"),'Profesor':1})
			titulo="Sanciones"
		else:
			return redirect("/")
		error=False
	context={'alum':alum,'form':form,'titulo':titulo,'tipo':tipo}
	return render(request, 'parte.html',context)