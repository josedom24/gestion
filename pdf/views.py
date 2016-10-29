import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from xhtml2pdf import pisa
from cStringIO import StringIO
from centro.models import Alumnos,Cursos
from centro.views import ContarFaltas


# Create your views here.


@login_required(login_url='/')
def imprimir_partes(request,curso):
	lista_alumnos = Alumnos.objects.filter(Unidad__id=curso)
	lista=zip(range(1,len(lista_alumnos)+1),lista_alumnos,ContarFaltas(lista_alumnos.values("id")))
	data={'alumnos':lista,'curso':Cursos.objects.get(id=curso)}
	# Render html content through html template with context
	return imprimir("partes.html",data,"partes.pdf")




	
def imprimir(temp,data,tittle):
	template = get_template(temp)
	pdf_data = template.render(Context(data))
	# Write PDF to file
	
	pdf = StringIO()
	pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
	pdf.reset()
	response = HttpResponse(pdf.read(),content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="'+tittle+'"'
	return response
