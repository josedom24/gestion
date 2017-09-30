
# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from convivencia.forms import AmonestacionForm,SancionForm,FechasForm
from centro.models import Alumnos,Profesores
from centro.views import group_check_je
from convivencia.models import Amonestaciones,Sanciones,TiposAmonestaciones
from centro.models import Cursos
from django.contrib.auth.decorators import login_required,user_passes_test
from correo.models import Correos
import time,calendar
from datetime import datetime
from operator import itemgetter
from django.db.models import Count
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
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
			
			if tipo=="amonestacion":
				amon=form.instance
				destinatarios=[amon.Profesor,amon.IdAlumno.Unidad.Tutor]
				
				template = get_template("correo_amonestacion.html")
				contenido = template.render(Context({'amon':amon}))
				new_correo=Correos(Fecha=time.strftime("%Y-%m-%d"),Asunto="Nueva amonestación",Contenido=contenido)
				new_correo.save()
				for dest in destinatarios:
					if dest!=None:
						new_correo.Destinatarios.add(dest)
				new_correo.save()

			if tipo=="sancion":
				sanc=form.instance
				destinatarios=sanc.IdAlumno.Unidad.EquipoEducativo
				template = get_template("correo_sancion.html")
				contenido = template.render(Context({'sanc':sanc}))
				new_correo=Correos(Fecha=time.strftime("%Y-%m-%d"),Asunto="Nueva sanción",Contenido=contenido)
				new_correo.save()
				for dest in destinatarios.all():
					new_correo.Destinatarios.add(dest)
				new_correo.save()
			correos=[]
			for prof in new_correo.Destinatarios.all():
				correo = Profesores.objects.get(id=prof.id).Email
				if correo!="":
					correos.append(correo)
				print correo
			send_mail(
                new_correo.Asunto,
                new_correo.Contenido,
                '41011038.edu@juntadeandalucia.es',
                correos,
                fail_silently=False,
               )
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
	context={'alum':alum,'form':form,'titulo':titulo,'tipo':tipo,'menu_alumnos':True}
	return render(request, 'parte.html',context)



@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def historial(request,alum_id,prof):
	horas=["1ª hora","2ª hora","3ª hora","Recreo","4ª hora","5ª hora","6ª hora"]
	alum=Alumnos.objects.get(pk=alum_id)
	amon=Amonestaciones.objects.filter(IdAlumno_id=alum_id).order_by('Fecha')
	sanc=Sanciones.objects.filter(IdAlumno_id=alum_id).order_by("Fecha")
	
	historial=list(amon)+list(sanc)
	historial=sorted(historial, key=lambda x: x.Fecha, reverse=False)
	
	tipo=[]
	for h in historial:
		if str(type(h)).split(".")[2][0]=="A":
			tipo.append("Amonestación")
		else:
			tipo.append("Sanción")
	hist=zip(historial,tipo,range(1,len(historial)+1))
	prof=True if prof=="" else False
	context={'prof':prof,'alum':alum,'historial':hist,'menu_historial':True,'horas':horas}
	return render(request, 'historial.html',context)


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def resumen_hoy(request,tipo):
	hoy=datetime.now()
	return resumen(request,tipo,str(hoy.month),str(hoy.year))


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def resumen(request,tipo,mes,ano):
	if request.method=='POST':
		tipo=request.POST.get('tipo')

	c = calendar.HTMLCalendar(calendar.MONDAY)
	calhtml=c.formatmonth(int(ano),int(mes))

	if tipo=="amonestacion":
		datos=Amonestaciones.objects.filter(Fecha__year=ano).filter(Fecha__month=mes)
		titulo="Resumen de amonestaciones"
	if tipo=="sancion":
		datos=Sanciones.objects.filter(Fecha__year=ano).filter(Fecha__month=mes)
		titulo="Resumen de sanciones"
	
	ult_dia=calendar.monthrange(int(ano),int(mes))[1]
	dic_fechas=datos.values("Fecha")
	fechas=[]
	for f in dic_fechas:
		fechas.append(f["Fecha"])

	for dia in xrange(1,int(ult_dia)+1):
		fecha=datetime(int(ano),int(mes),dia)
		if fecha.date() in fechas:
			calhtml=calhtml.replace(">"+str(dia)+"<",'><a href="/convivencia/show/%s/%s/%s/%s"><strong>%s</strong></a><'%(tipo,mes,ano,dia,dia))
	calhtml=calhtml.replace('class="month"','class="table-condensed table-bordered table-striped"')
	#form=TipoResumen(initial={'tipo':tipo})
	
	
	mes_actual=datetime(int(ano),int(mes),1)
	mes_ant=AddMonths(mes_actual,-1)
	mes_prox=AddMonths(mes_actual,1)

	context={'calhtml':calhtml,'fechas':[mes_actual,mes_ant,mes_prox],'titulo':titulo,'tipo':tipo,'menu_resumen':True}
	return render(request, 'resumen.html',context)

def AddMonths(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = d.year + ((( d.month - 1) + x ) / 12 ) 
    return datetime( newyear, newmonth, d.day)

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def show(request,tipo,mes,ano,dia):
	fecha=datetime(int(ano),int(mes),int(dia))
	if tipo=="amonestacion":
		datos=Amonestaciones.objects.filter(Fecha=fecha)
		titulo="Resumen de amonestaciones"
	if tipo=="sancion":
		datos=Sanciones.objects.filter(Fecha=fecha)
		titulo="Resumen de sanciones"
	
	datos=zip(range(1,len(datos)+1),datos,ContarFaltas(datos.values("IdAlumno")))
	context={'datos':datos,'tipo':tipo,'fecha':fecha,'titulo':titulo,'menu_'+tipo:True}
	context[tipo]=True
	return render(request, 'show.html',context)

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def estadisticas(request):

	if request.method=="POST":
		
		f1=datetime(int(request.POST.get('Fecha1_year')),int(request.POST.get('Fecha1_month')),int(request.POST.get('Fecha1_day')))
		f2=datetime(int(request.POST.get('Fecha2_year')),int(request.POST.get('Fecha2_month')),int(request.POST.get('Fecha2_day')))
		a1t=Amonestaciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count()
		s1t=Sanciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count()
		datos=a1t,s1t
		fechas=[f1,f2]
		form=FechasForm(request.POST)
		total=()
		#Tipos de amonestaciones
		tipos=[]
		for i in TiposAmonestaciones.objects.all():
			tipos.append((i.TipoAmonestacion,
						Amonestaciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).filter(Tipo=i).count(),
						))
		filtro=True
	else:
		year1=Amonestaciones.objects.first().Fecha.year
		fi1=datetime(year1,9,1)
		ff1=datetime(year1,12,31)
		fi2=datetime(year1+1,1,1)
		ff2=datetime(year1+1,3,31)
		fi3=datetime(year1+1,4,1)
		ff3=datetime(year1+1,6,30)

		a1t=Amonestaciones.objects.filter(Fecha__gte=fi1).filter(Fecha__lte=ff1).count()
		a2t=Amonestaciones.objects.filter(Fecha__gte=fi2).filter(Fecha__lte=ff2).count()
		a3t=Amonestaciones.objects.filter(Fecha__gte=fi3).filter(Fecha__lte=ff3).count()
		s1t=Sanciones.objects.filter(Fecha__gte=fi1).filter(Fecha__lte=ff1).count()
		s2t=Sanciones.objects.filter(Fecha__gte=fi2).filter(Fecha__lte=ff2).count()
		s3t=Sanciones.objects.filter(Fecha__gte=fi3).filter(Fecha__lte=ff3).count()
		datos=a1t,s1t,a2t,s2t,a3t,s3t
		form=FechasForm()
		fechas=[fi1,ff3]
		total=Amonestaciones.objects.count(),Sanciones.objects.count()
		filtro=False

		#Tipos de amonestaciones
		tipos=[]
		for i in TiposAmonestaciones.objects.all():
			tipos.append((i.TipoAmonestacion,
						Amonestaciones.objects.filter(Fecha__gte=fi1).filter(Fecha__lte=ff1).filter(Tipo=i).count(),
						Amonestaciones.objects.filter(Fecha__gte=fi2).filter(Fecha__lte=ff2).filter(Tipo=i).count(),
						Amonestaciones.objects.filter(Fecha__gte=fi3).filter(Fecha__lte=ff3).filter(Tipo=i).count(),
						))

	context={'filtro':filtro,'tipos':tipos,'total':total,'form':form,'datos':datos,'fechas':fechas,'menu_estadistica':True}
	return render(request,'estadisticas.html',context)
    

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def horas(request):
	if request.method=="POST":
		f1=datetime(int(request.POST.get('Fecha1_year')),int(request.POST.get('Fecha1_month')),int(request.POST.get('Fecha1_day')))
		f2=datetime(int(request.POST.get('Fecha2_year')),int(request.POST.get('Fecha2_month')),int(request.POST.get('Fecha2_day')))
	lista=[]
	horas=["Primera","Segunda","Tercera","Recreo","Cuarta","Quinta","Sexta"]
	for i in xrange(1,8):
		if request.method=="POST":
			lista.append(Amonestaciones.objects.filter(Hora=i).filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
		else:
			lista.append(Amonestaciones.objects.filter(Hora=i).count())
	form=FechasForm(request.POST) if request.method=="POST" else FechasForm()
	horas.append("Total")
	if request.method=="POST":
		lista.append(Amonestaciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
	else:
		lista.append(Amonestaciones.objects.count())

	context={'form':form,'horas':zip(horas,lista),'menu_estadistica':True}
	return render(request,'horas.html',context)
	
@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def profesores(request):
	if request.method=="POST":
		f1=datetime(int(request.POST.get('Fecha1_year')),int(request.POST.get('Fecha1_month')),int(request.POST.get('Fecha1_day')))
		f2=datetime(int(request.POST.get('Fecha2_year')),int(request.POST.get('Fecha2_month')),int(request.POST.get('Fecha2_day')))
	lista=[]
	if request.method=="POST":
		listAmon=Amonestaciones.objects.values('Profesor').filter(Fecha__gte=f1).filter(Fecha__lte=f2).annotate(Count('Profesor'))
	else:
		listAmon=Amonestaciones.objects.values('Profesor').annotate(Count('Profesor'))
	newlist = sorted(listAmon, key=itemgetter('Profesor__count'), reverse=True)
	suma=0
	for l in newlist:
		l["Profesor"]=Profesores.objects.get(id=l["Profesor"]).Apellidos+", "+Profesores.objects.get(id=l["Profesor"]).Nombre
		suma+=l["Profesor__count"]
	form=FechasForm(request.POST) if request.method=="POST" else FechasForm()
	context={"form":form,"lista":newlist,'menu_estadistica':True,"suma":suma}
	return render(request,'lprofesores.html',context)


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def grupos(request):
	cursos=Cursos.objects.order_by('Curso')
	if request.method=="POST":
		f1=datetime(int(request.POST.get('Fecha1_year')),int(request.POST.get('Fecha1_month')),int(request.POST.get('Fecha1_day')))
		f2=datetime(int(request.POST.get('Fecha2_year')),int(request.POST.get('Fecha2_month')),int(request.POST.get('Fecha2_day')))
	

	#Total
	total=[]
	if request.method=="POST":
		total.append(Amonestaciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
		total.append(Sanciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
	else:
		total.append(Amonestaciones.objects.count())
		total.append(Sanciones.objects.count())

	lista=[]
	
	for curso in cursos:

		if request.method=="POST":
			datos=[Amonestaciones.objects.filter(IdAlumno__in=Alumnos.objects.filter(Unidad=curso)).filter(Fecha__gte=f1).filter(Fecha__lte=f2).count(),
				Sanciones.objects.filter(IdAlumno__in=Alumnos.objects.filter(Unidad=curso)).filter(Fecha__gte=f1).filter(Fecha__lte=f2).count()]
		else:
			datos=[Amonestaciones.objects.filter(IdAlumno__in=Alumnos.objects.filter(Unidad=curso)).count(),
				Sanciones.objects.filter(IdAlumno__in=Alumnos.objects.filter(Unidad=curso)).count()]
		datos.append(datos[0]*100/total[0])
		datos.append(datos[1]*100/total[1])
		lista.append(datos)
	form=FechasForm(request.POST) if request.method=="POST" else FechasForm()
	
	cursos=zip(cursos,lista)
	cursos=sorted(cursos, key=lambda x: x[1][0], reverse=True)
	context={'form':form,'cursos':cursos,'menu_estadistica':True,'total':total}
	return render(request,'grupos.html',context)
	

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def alumnos(request):
	
	if request.method=="POST":
		f1=datetime(int(request.POST.get('Fecha1_year')),int(request.POST.get('Fecha1_month')),int(request.POST.get('Fecha1_day')))
		f2=datetime(int(request.POST.get('Fecha2_year')),int(request.POST.get('Fecha2_month')),int(request.POST.get('Fecha2_day')))
	

	#Total
	total=[]
	if request.method=="POST":
		total.append(Amonestaciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
		total.append(Sanciones.objects.filter(Fecha__gte=f1).filter(Fecha__lte=f2).count())
	else:
		total.append(Amonestaciones.objects.count())
		total.append(Sanciones.objects.count())

	

	if request.method=="POST":
		listAmon=Amonestaciones.objects.values('IdAlumno').filter(Fecha__gte=f1).filter(Fecha__lte=f2).annotate(Count('IdAlumno'))
		listSan=Sanciones.objects.values('IdAlumno').filter(Fecha__gte=f1).filter(Fecha__lte=f2).annotate(Count('IdAlumno'))
	else:
		listAmon=Amonestaciones.objects.values('IdAlumno').annotate(Count('IdAlumno'))
		listSan=Sanciones.objects.values('IdAlumno').annotate(Count('IdAlumno'))
	newlist = sorted(listAmon, key=itemgetter('IdAlumno__count'), reverse=True)
	for l in newlist:
		try:
			l["Sanciones"]=listSan.get(IdAlumno=l["IdAlumno"]).get("IdAlumno__count")
		except:
			l["Sanciones"]=0
		l["Porcentajes"]=[]
		try:
			l["Porcentajes"].append(l["IdAlumno__count"]*100/total[0])
		except:
			l["Porcentajes"].append(0)
		try:
			l["Porcentajes"].append(l["Sanciones"]*100/total[1])
		except:
			l["Porcentajes"].append(0)
		l["IdAlumno"]=Alumnos.objects.get(id=l["IdAlumno"]).Nombre+" ("+Alumnos.objects.get(id=l["IdAlumno"]).Unidad.Curso+")"
	form=FechasForm(request.POST) if request.method=="POST" else FechasForm()
	context={"form":form,"lista":newlist,'menu_estadistica':True,"suma":total}
	return render(request,'lalumnos.html',context)

	

def ContarFaltas(lista_id):
	contar=[]
	for alum in lista_id:

		am=str(len(Amonestaciones.objects.filter(IdAlumno_id=alum.values()[0])))
		sa=str(len(Sanciones.objects.filter(IdAlumno_id=alum.values()[0])))

		contar.append(am+"/"+sa)
	return contar
