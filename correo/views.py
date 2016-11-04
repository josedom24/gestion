from django.shortcuts import render
from coreos.models import Correos
# Create your views here.

@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def list_correos(request):
    lista_correos=Correos.object.all()
    form=CorreosForm()
    return ""


@login_required(login_url='/')
@user_passes_test(group_check_je,login_url='/')
def new_correo(request):

