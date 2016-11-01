from django.shortcuts import render,redirect
from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
from datetime import datetime
from registro.forms import RegistroForm,BuscarRegistroForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from centro.views import group_check_sec

import time
# Create your views here.

@login_required(login_url='/')
@user_passes_test(group_check_sec,login_url='/')
def registro(request,tipo):
	curso=CalcularCurso()
	
	dict={'Tipo':tipo,'Curso':curso}

	form = BuscarRegistroForm()
	error=False
	if request.method=='GET'and request.GET.has_key("Curso"):
		print request.GET
		form = BuscarRegistroForm(request.GET)
		error=True

		if form.is_valid():
			datos=form.cleaned_data
			print datos
			if datos['Procedencia']!="" and datos['Procedencia']!=None:
				dict["Idp"]=datos['Procedencia']
			if datos['Curso']!="" and datos['Curso']!=None:
				dict["Curso"]=datos['Curso']
			if datos['Remitente']!="" and datos['Remitente']!=None:
				dict["Idr"]=datos['Remitente']
			if datos['Documento']!="" and datos['Documento']!=None:
				dict["Idc"]=datos['Documento']
			if datos['Desde']!="" and datos['Desde']!=None:
				dict["Fecha__gte"]=datos['Desde']
			if datos['Hasta']!="" and datos['Hasta']!=None:
				dict["Fecha__lte"]=datos['Hasta']
			if datos['Contenido']!="" and datos['Contenido']!=None:
				dict["Contenido__contains"]=datos['Contenido']
			

		
	print dict
	reg=Registro.objects.filter(**dict).order_by("-N")
	paginator = Paginator(reg, 10)
	
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
		request.GET._mutable = True
		if request.GET.get('page'):
			request.GET.pop('page')
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	

	context={'reg':contacts,'tipo':tipo,'curso':curso,'form':form,'error':error,'busqueda':'&'+request.GET.urlencode(),'menu_registro':True}
	return render(request, 'registro.html',context)


@login_required(login_url='/')
@user_passes_test(group_check_sec,login_url='/')
def add(request,tipo):
	
	if request.method=='POST':
		N=request.POST.get('N')
		curso=request.POST.get('curso')
		form = RegistroForm(request.POST)
		error=True
		if form.is_valid():
			form.save()
			return redirect('/registro/'+tipo)
	else:
		curso=CalcularCurso()
		dict={'Tipo':tipo,'Curso':curso}
		reg=Registro.objects.filter(**dict).order_by("-N").first()
		if reg.N>1:
			N=reg.N+1
		else:
			N=reg.N
		form = RegistroForm({'N':N,'Curso':curso,'Tipo':tipo,'Fecha':time.strftime("%d/%m/%Y"),'Idp':1,'Idr':1,'Idc':1})
		error=False
	context={'N':N,'curso':curso,'tipo':tipo,'form':form,'error':error}
	return render(request, 'add.html',context)






def CalcularCurso():
	hoy=datetime.now()
	if hoy.month>=9:
		curso=str(hoy.year)+"-"+str(hoy.year+1)
	else:
		curso=str(hoy.year-1)+'-'+str(hoy.year)
	return curso