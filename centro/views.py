from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from centro.models import Alumnos,Cursos,Departamentos,Profesores
from convivencia.models import Amonestaciones,Sanciones
from centro.forms import UnidadForm,DepartamentosForm

# Create your views here.
@login_required(login_url='/')
def alumnos(request):
	if request.method == 'POST':
		primer_id=request.POST.get("Unidad")
	else:
		primer_id=request.session.get('Unidad', Cursos.objects.order_by('Curso').first().id)
	request.session['Unidad']=primer_id
		
	lista_alumnos = Alumnos.objects.filter(Unidad__id=primer_id)
	form = UnidadForm({'Unidad':primer_id})
	#lista=zip(lista_alumnos,funciones.ContarFaltas(lista_alumnos.values("id")),funciones.ContarAmonestacionesAcumuladas(lista_alumnos.values("id")),range(1,len(lista_alumnos)+1))
	lista=zip(range(1,len(lista_alumnos)+1),lista_alumnos,ContarFaltas(lista_alumnos.values("id")))
	context={'alumnos':lista,'form':form,'curso':Cursos.objects.get(id=primer_id).Curso}
	return render(request, 'alumnos.html',context)


@login_required(login_url='/')
def profesores(request):
	if request.method == 'POST':
		dep_id=request.POST.get("Departamento")
	else:
		dep_id=request.session.get('Departamento', "")
	request.session['Departamento']=dep_id
		
	if dep_id=="":
		lista_profesores = Profesores.objects.all()
		departamento=""
	else:
		lista_profesores = Profesores.objects.filter(Departamento__id=dep_id)
		departamento=Departamentos.objects.get(id=dep_id).Nombre
	form = DepartamentosForm({'Departamento':dep_id})
	cursos=Tutorias(lista_profesores.values("id"))
	
	#lista=zip(lista_alumnos,funciones.ContarFaltas(lista_alumnos.values("id")),funciones.ContarAmonestacionesAcumuladas(lista_alumnos.values("id")),range(1,len(lista_alumnos)+1))
	lista=zip(lista_profesores,range(1,len(lista_profesores)+1),cursos)
	context={'profesores':lista,'form':form,"departamento":departamento}
	return render(request, 'profesor.html',context)
	
def ContarFaltas(lista_id):
	contar=[]
	for alum in lista_id:

		am=str(len(Amonestaciones.objects.filter(IdAlumno_id=alum.values()[0])))
		sa=str(len(Sanciones.objects.filter(IdAlumno_id=alum.values()[0])))
		
		contar.append(am+"/"+sa)
	return contar

def Tutorias(lista_id):
	cursos=[]
	for prof in lista_id:
		try:
			cursos.append(Cursos.objects.get(Tutor=prof.values()[0]).Curso)
		except Exception, e:
			cursos.append("")
	return cursos