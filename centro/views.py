# -*- coding: utf-8 -*-
from django.shortcuts import render
from centro.models import Alumnos,AltaAlumnos,Cursos
from convivencia.models import Amonestaciones,Sanciones
from centro.forms import UnidadForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from funciones import funciones
@login_required(login_url='/admin/login/')
def index(request):
	if request.method == 'POST':
		primer_id=request.POST.get("Unidad")
	else:
		primer_id=request.session.get('Unidad', Cursos.objects.order_by('Curso').first().id)
	request.session['Unidad']=primer_id
		
	lista_alumnos = Alumnos.objects.filter(Unidad__id=primer_id)
	form = UnidadForm({'Unidad':primer_id})
	lista=zip(lista_alumnos,funciones.ContarFaltas(lista_alumnos.values("id")),range(1,len(lista_alumnos)+1))
	context={'alumnos':lista,'form':form}
	return render(request, 'centro/centro.html',context)


@login_required(login_url='/admin/login/')
def logout_view(request):
    logout(request)
    return redirect('/')
@login_required(login_url='/admin/login/')
def alta(request):
	ficheros= AltaAlumnos.objects.all()
	if len(ficheros)>1:
		context={'msg':'Sólo puedes subir un fichero de alta másiva.'}
		return render(request, 'centro/alta.html',context)
	if len(ficheros)==0:
		context={'msg':'Tienes que subir un fichero de alta másiva de alumnos.'}
		return render(request, 'centro/alta.html',context)

	f=open(settings.MEDIA_ROOT+'/'+ficheros.values_list()[0][1],"r")
	
	alumnos=f.readlines()
	alumnos2=[]
	for alum in alumnos:
		alum=alum.split("|")
		alumnos2.append(alum)
	
	cont=0
	for alum in alumnos2:
		cont=cont+1
		valores=[]
		valores.append(None)
		for al in alum:
			valores.append(al.rstrip())
		new_alum=Alumnos(*valores)
		new_alum.Fecha_nacimiento=datetime.datetime.strptime(new_alum.Fecha_nacimiento, "%d/%m/%Y").strftime("%Y-%m-%d")
		
		try:
			c=Cursos.objects.get(Curso=valores[8])
		except ObjectDoesNotExist:
			c=Cursos(Curso=valores[8])
    		c.save()
    		new_alum.Unidad=c
    		new_alum.save()
    	else:
    		new_alum.Unidad=c
    		new_alum.save()
    	
	context={'msg':'Empezamos el alta másiva','fich':cont}
	return render(request, 'centro/alta.html',context)

