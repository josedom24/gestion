from django.shortcuts import render,redirect
from correo.models import Correos
from centro.models import Cursos,Departamentos,Areas
from django.contrib.auth.decorators import login_required,user_passes_test
from centro.views import group_check_je
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from correo.forms import CorreoForm,BuscarDestinatariosForm
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
    if request.method=='POST' and not request.POST.has_key("correo"):
        form2 = BuscarDestinatariosForm(request.POST)
        form = CorreoForm({'Asunto':request.POST.get("Asunto"),'Contenido':request.POST.get("Contenido"),'Destinatarios':SelectProfes(int(request.POST.get("Profesores"))),'Fecha':time.strftime("%d/%m/%Y")})

    elif request.method=='POST' and request.POST.has_key("correo"):
        form2 = BuscarDestinatariosForm(request.POST.get("Profesores")) 
        form = CorreoForm(request.POST)
        if form.is_valid():
            form.save()
            correos=[]
            for prof in request.POST["Destinatarios"]:
                correos.append(Profesores.objects.get(id=prof).Email)


            send_mail(
                   request.POST["Asunto"],
                   request.POST["Contenido"],
                   '41011038.jestudios.edu@juntadeandalucia.es',
                 #  'josedom24@gmail.com',
                   correos,
                   fail_silently=False,
                  )
            return redirect('/correo/list')
    else:
        form = CorreoForm({'Destinatarios':Profesores.objects.none(),'Fecha':time.strftime("%d/%m/%Y")})
        form2 = BuscarDestinatariosForm()
    context={'form2':form2,'form':form,'menu_correos':True}
    return render(request, 'add_correos.html',context)

def SelectProfes(id):
    cursos=Cursos.objects.all().order_by("Curso")
    departamentos=Departamentos.objects.all().order_by("Nombre")
    areas=Areas.objects.all().order_by("Nombre")
    if id==0:
        return Profesores.objects.none()
    if id==1:
        return Profesores.objects.all()
    if id==2:
        return Profesores.objects.filter(Etcp=1)
    if id==3:
        return Profesores.objects.filter(Ce=1)
    if id==4:
        return Profesores.objects.filter(Bil=1)
    if id>=5 and id<=21:
        return [Cursos.objects.get(Curso=cursos[id-5].Curso).Tutor]
    if id>=22 and id<=38:
        return Cursos.objects.get(Curso=cursos[id-22].Curso).EquipoEducativo.all()
    if id>=39 and id<=58:
        return Profesores.objects.filter(Departamento=departamentos[id-39].id)
    if id>=59 and id<=62:
        lista=[]
        for dep in Areas.objects.get(id=areas[id-59].id).Departamentos.all():
            lista.extend(Profesores.objects.filter(Departamento=dep.id))
        return lista
    return Profesores.objects.none()

