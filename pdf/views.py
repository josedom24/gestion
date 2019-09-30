import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test

from xhtml2pdf import pisa
from centro.models import Alumnos,Cursos,Profesores
from convivencia.models import Amonestaciones,Sanciones
from registro.models import Registro 
from centro.views import ContarFaltas,group_check_je,group_check_sec
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
# Create your views here.


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_partes(request,curso):
    lista_alumnos = Alumnos.objects.filter(Unidad__id=curso)
    lista_alumnos=sorted(lista_alumnos,key=lambda d: d.Nombre)
    ids=[{"id":elem.id} for elem in lista_alumnos]
    lista=zip(range(1,len(lista_alumnos)+1),lista_alumnos,ContarFaltas(ids))
    data={'alumnos':lista,'curso':Cursos.objects.get(id=curso),'fecha':datetime.now()}
    # Render html content through html template with context
    return imprimir("pdf_partes.html",data,"partes.pdf")

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_faltas(request,curso):
    lista_alumnos = Alumnos.objects.filter(Unidad__id=curso)
    lista_alumnos=sorted(lista_alumnos,key=lambda d: d.Nombre)
    data={'alumnos':lista_alumnos,'curso':Cursos.objects.get(id=curso),'cont':range(0,30)}
    # Render html content through html template with context
    return imprimir("pdf_faltas.html",data,"faltas.pdf")

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_telefonos(request,curso):
	lista_alumnos = Alumnos.objects.filter(Unidad__id=curso)
	lista_alumnos=sorted(lista_alumnos,key=lambda d: normalize(d.Nombre))
	lista=zip(range(1,len(lista_alumnos)+1),lista_alumnos)
	data={'alumnos':lista,'curso':Cursos.objects.get(id=curso),'fecha':datetime.now()}
	# Render html content through html template with context
	return imprimir("pdf_telefonos.html",data,"telefonos.pdf")
@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_historial(request,alum_id,prof):
    horas=["1ª hora","2ª hora","3ª hora","Recreo","4ª hora","5ª hora","6ª hora"]
    alum=Alumnos.objects.get(pk=alum_id)
    amon=Amonestaciones.objects.filter(IdAlumno_id=alum_id).order_by('Fecha')
    sanc=Sanciones.objects.filter(IdAlumno_id=alum_id).order_by("Fecha")
    
    historial=list(amon)+list(sanc)
    historial=sorted(historial, key=lambda x: x.Fecha, reverse=False)
    
    tipo=[]
    for h in historial:
        if str(type(h)).split(".")[2][0]=="A":
            tipo.append("A")
        else:
                    tipo.append("S")
    hist=zip(historial,tipo,range(1,len(historial)+1))
    prof=True if prof=="" else False
    data={'alum':alum,'historial':hist,'horas':horas,'prof':prof}
    return imprimir("pdf_historial.html",data,"historial.pdf")

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_show(request,tipo,mes,ano,dia):
    fecha=datetime(int(ano),int(mes),int(dia))
    if tipo=="amonestacion":
        datos=Amonestaciones.objects.filter(Fecha=fecha)
        titulo="Resumen de amonestaciones"
    if tipo=="sancion":
        datos=Sanciones.objects.filter(Fecha=fecha)
        titulo="Resumen de sanciones"
    
    datos=zip(range(1,len(datos)+1),datos,ContarFaltas(datos.values("IdAlumno")))
    
    data={'datos':datos,'tipo':tipo,'fecha':fecha,'titulo':titulo,tipo:True}
    return imprimir("pdf_resumen.html",data,"resumen_"+tipo+".pdf")	

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_sanciones_hoy(request):
    hoy=datetime.now()
    dict={}
    dict["Fecha_fin__gte"]=hoy
    dict["Fecha__lte"]=hoy
    datos=Sanciones.objects.filter(**dict).order_by("Fecha")
    titulo="Alumnos sancionados"
    datos=zip(range(1,len(datos)+1),datos,[x for x in datos])
    data={'datos':datos,'tipo':"sancion",'fecha':hoy,'titulo':titulo}
    return imprimir("pdf_resumen.html",data,"resumen_sancion_hoy.pdf")	

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def carta_amonestacion(request,mes,ano,dia,todos):
    info={}
    contenido=""
    fecha2=datetime(int(ano),int(mes),int(dia))
    info["fecha"]="%s/%s/%s"%(dia,mes,ano)
    #lista_alumnos=set(Amonestaciones.objects.filter(Fecha=fecha2).values_list("IdAlumno"))
    lista_amonestaciones = Amonestaciones.objects.filter(Fecha=fecha2)
    info["amonestaciones"]=[]
    for amonestacion in lista_amonestaciones:
        if todos=="n" and amonestacion.IdAlumno.email=="":
            info["amonestaciones"].append(amonestacion)
        if todos=="s":
            info["amonestaciones"].append(amonestacion)

    for a in info["amonestaciones"]:
        info2={}
        info2["amonestacion"]=a
        info2["num_amon"]=len(Amonestaciones.objects.filter(IdAlumno_id=a.IdAlumno.id))
        template = get_template("pdf_contenido_carta_amonestacion.html")
        contenido=contenido+ template.render(Context(info2))
        if a.IdAlumno.id!=info["amonestaciones"][-1].id:
            contenido=contenido+"<pdf:nextpage>"
    info["contenido"]=contenido
    return imprimir("pdf_carta.html",info,"carta_amonestacion"+".pdf")	


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def send_amonestacion(request,mes,ano,dia):
    info={}
    contenido=""
    fecha2=datetime(int(ano),int(mes),int(dia))
    info["fecha"]="%s/%s/%s"%(dia,mes,ano)
    lista_alumnos=set(Amonestaciones.objects.filter(Fecha=fecha2).values_list("IdAlumno"))
    lista_amonestaciones=Amonestaciones.objects.filter(Fecha=fecha2)
    info["amonestaciones"]=[]
    for alum in lista_alumnos:
        if Alumnos.objects.get(id=alum[0]).email!="":
            info["amonestaciones"].append(Alumnos.objects.get(id=alum[0]))

    for i in info["amonestaciones"]:
        info2={}
        info2["amonestacion"]=i
        info2["num_amon"]=len(Amonestaciones.objects.filter(IdAlumno_id=i.id))
        template = get_template("pdf_contenido_carta_amonestacion.html")
        contenido=contenido+ template.render(Context(info2))
        asunto="IES Gonzalo Nazareno. Amonestación: "+i.Nombre.encode("utf-8")
        
        msg = EmailMultiAlternatives(
                asunto,
                contenido,
                '41011038.edu@juntadeandalucia.es',
                [i.email]
               )
        msg.attach_alternative(contenido, "text/html")
        msg.send(fail_silently=False)
    context={"info":info}
    return render(request,"send_amonestacion.html",context)

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def carta_sancion(request,identificador):
    info2={}
    contenido=""
    
    info2["sancion"]=Sanciones.objects.get(id=identificador)
    info={}
    template = get_template("pdf_contenido_carta_sancion.html")
    info["contenido"]=template.render(Context(info2))	
    return imprimir("pdf_carta.html",info,"carta_sancion"+".pdf")	


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def imprimir_profesores(request,curso=None):

	lista_profesores = Profesores.objects.all().exclude(Apellidos="-").order_by("Apellidos")
	texto="Listado de profesores"
	if request.path.split("/")[2]=="claustro":
		if curso==None:
			lista_profesores=lista_profesores.exclude(Baja=True)
			texto='Asistencia a claustro'
		else:
			c=Cursos.objects.get(id=curso)
			lista_profesores=c.EquipoEducativo.all()
			texto='Asistencia a Equipo Educativo de '+c.Curso
		data={'texto':texto,'profesores':lista_profesores,'fecha':datetime.now(),"resto":len(lista_profesores) % 3}
	elif request.path.split("/")[2]=="semana":
		lista_profesores=lista_profesores.exclude(Baja=True)
		texto='Asistencia semanal'
		data={'texto':texto,'profesores':lista_profesores,'fecha':datetime.now(),"resto":len(lista_profesores) % 3}
	# Render html content through html template with context
	return imprimir("pdf_"+request.path.split("/")[2]+".html",data,request.path.split("/")[2]+".pdf")


@login_required(login_url='/')
@user_passes_test(group_check_sec,login_url='/')
def imprimir_registro(request,tipo,curso):
    
    dict={'Tipo':tipo,'Curso':curso}

    reg=Registro.objects.filter(**dict).order_by("-N")
    data={'reg':reg,'tipo':tipo,'curso':curso}
    return imprimir("pdf_registro.html",data,"registro_"+tipo+"_"+curso+".pdf")



def imprimir(temp,data,tittle):
    template = get_template(temp)
    pdf_data = template.render(data)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+tittle+'"'
    try:
        pisa.CreatePDF(pdf_data, dest=response)
    except:
        return HttpResponse('Errors')
    return response
