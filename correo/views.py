from django.shortcuts import render
from correo.models import Correos
from django.contrib.auth.decorators import login_required,user_passes_test
from centro.views import group_check_je
# Create your views here.

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def list_correo(request):
    lista_correos=Correos.object.all()
    form=CorreosForm()
    return ""


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def new_correo(request):
    pass
