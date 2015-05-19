from django.shortcuts import render
from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
from datetime import datetime
from registro.forms import RegistroForm,BuscarRegistroForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required(login_url='/admin/login/')
def registro(request,tipo):
	hoy=datetime.now()
	if hoy.month>=9:
		curso=str(hoy.year)+"-"+str(hoy.year+1)
	else:
		curso=str(hoy.year-1)+'-'+str(hoy.year)

	dict={'Tipo':tipo,'Curso':curso}


	if request.method=='GET':
		
		form = BuscarRegistroForm(request.GET)
		error=True
		if form.is_valid():
			datos=form.cleaned_data
			if datos['Procedencia']!="" and datos['Procedencia']!=None:
				dict["Idp"]=datos['Procedencia']
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
			
	else:
		form = BuscarRegistroForm()
		error=False

	
	
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
	

	context={'reg':contacts,'tipo':tipo,'curso':curso,'form':form,'error':error,'busqueda':'&'+request.GET.urlencode()}
	return render(request, 'registro/registro.html',context)



	#reg=Registro.objects.filter(Tipo='e').filter(Curso=curso).aggregate(Max('N'))
#	N=reg['N__max']+1
#	#

#	form = RegistroForm({'Curso':curso,'Fecha':time.strftime("%d/%m/%Y"),'N':N,'Tipo':tipo})
#	error=False
#	context={'reg':reg,'form':form,'error':error}
#	return render(request, 'registro/registro.html',context)