from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from centro.models import Alumnos,Cursos,Departamentos,Profesores
from convivencia.models import Amonestaciones,Sanciones
from centro.forms import UnidadForm,DepartamentosForm
from datetime import datetime
from unicodedata import lookup, name




def group_check_je(user):
    return user.groups.filter(name__in=['jefatura de estudios'])
def group_check_sec(user):
    return user.groups.filter(name__in=['secretaria'])

# Create your views here.
@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def alumnos(request):
        
	if request.method == 'POST':
		primer_id=request.POST.get("Unidad")
	else:
		try:
			primer_id=request.session.get('Unidad', Cursos.objects.order_by('Curso').first().id)
		except:
			primer_id=0

	request.session['Unidad']=primer_id

	lista_alumnos = Alumnos.objects.filter(Unidad__id=primer_id)
	lista_alumnos=sorted(lista_alumnos,key=lambda d: normalize(d.Nombre))
	ids=[{"id":elem.id} for elem in lista_alumnos]

	form = UnidadForm({'Unidad':primer_id})
	#lista=zip(lista_alumnos,funciones.ContarFaltas(lista_alumnos.values("id")),funciones.ContarAmonestacionesAcumuladas(lista_alumnos.values("id")),range(1,len(lista_alumnos)+1))
	lista=zip(lista_alumnos,ContarFaltas(ids),EstaSancionado(ids))
	try:
		context={'alumnos':lista,'form':form,'curso':Cursos.objects.get(id=primer_id),'menu_alumnos':True}
	except:
		context={'alumnos':lista,'form':form,'curso':None,'menu_alumnos':True}
	return render(request, 'alumnos.html',context)


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def alumnos_curso(request,curso):
	request.POST = request.POST.copy()
	request.POST["Unidad"]=curso
	request.method="POST"
	return alumnos(request)


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def profesores(request):
	if request.method == 'POST':
		dep_id=request.POST.get("Departamento")
                area_id=request.POST.get("Areas")
                if area_id!=request.session.get("Areas",""):
                    dep_id=""
	else:
		dep_id=request.session.get('Departamento', "")
                area_id=request.session.get("Areas","")
	request.session['Areas']=area_id
	request.session['Departamento']=dep_id
        form=DepartamentosForm({'Areas':area_id,'Departamento':dep_id})
        if dep_id=="":
		lista_profesores = Profesores.objects.all().order_by("Apellidos")
		departamento=""
	else:
		lista_profesores = Profesores.objects.filter(Departamento__id=dep_id).order_by("Apellidos")
		departamento=Departamentos.objects.get(id=dep_id).Nombre
	cursos=Tutorias(lista_profesores.values("id"))
	
	#lista=zip(lista_alumnos,funciones.ContarFaltas(lista_alumnos.values("id")),funciones.ContarAmonestacionesAcumuladas(lista_alumnos.values("id")),range(1,len(lista_alumnos)+1))
	lista=zip(lista_profesores,cursos)
        context={'profesores':lista,'form':form,"departamento":departamento,'menu_profesor':True}
	return render(request, 'profesor.html',context)

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def profesores_change(request,campo,codigo,operacion):
	
	dato={}
	dato[campo]=True if operacion=="on" else False
	Profesores.objects.filter(id=codigo).update(**dato)
	
	return redirect("/centro/profesores")


	
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


def EstaSancionado(lista_id):
	estasancionado=[]
	hoy=datetime.now()
	dict={}
	dict["Fecha_fin__gte"]=hoy
	dict["Fecha__lte"]=hoy
	sanc=Sanciones.objects.filter(**dict).order_by("Fecha")
	listaid=[x.IdAlumno.id for x in sanc]
	for alum in lista_id:
		if alum.values()[0] in listaid:
			estasancionado.append(True)
		else:
			estasancionado.append(False)
	return estasancionado
		



@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def cursos(request):
	
	lista_cursos = Cursos.objects.all().order_by("Curso")
	
	
	
	context={'cursos':lista_cursos,'menu_cursos':True}
	return render(request, 'cursos.html',context)

def normalize(s, encoding = "UTF-8"):
    if not isinstance(s,unicode):
        s = s.decode(encoding)

    ret = u""
    for c in s:
        n = name(c)
        pos = n.find("WITH")
        if pos >= 0:
            n = n[:pos]
        n = lookup(n.strip())
        ret += n
    return ret