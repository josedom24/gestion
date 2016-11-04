from django.shortcuts import render,redirect
from correo.models import Correos
from django.contrib.auth.decorators import login_required,user_passes_test
from centro.views import group_check_je
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from correo.forms import CorreoForm
from convivencia.models import Profesores
from django.core.mail import send_mail
import time
# Create your views here.


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def list_correo(request):
    reg=Correos.objects.all().order_by("-id")
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
	
    context={'reg':contacts,'menu_correos':True}
    return render(request, 'list_correos.html',context)

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def new_correo(request):
    if request.method=='POST':
        form = CorreoForm(request.POST)
        if form.is_valid():
            form.save()
            correos=[]
            print request.POST
            for prof in request.POST["Destinatarios"]:
                correos.append(Profesores.objects.get(id=prof).Email)


            send_mail(
                   request.POST["Asunto"],
                   request.POST["Contenido"],
                 #  '41011038.edu@juntadeandalucia.es',
                   'josedom24@gmail.com',
                   correos,
                   fail_silently=False,
                  )
            return redirect('/correo/list')
    else:
        form = CorreoForm({'Destinatarios':Profesores.objects.filter(Departamento=17),'Fecha':time.strftime("%d/%m/%Y")})
       	context={'form':form,'menu_correos':True}
        return render(request, 'add_correos.html',context)

