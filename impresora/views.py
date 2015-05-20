from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from impresora.models import Carta
from django.template import Context, Template
from centro.models import Alumnos
from funciones import funciones


class carta(PDFTemplateView):
    template_name = "impresora/carta.html"


    def get_context_data(self, **kwargs):
    	c=Carta.objects.all().first()
    	a=Alumnos.objects.all().first()
    	template = Template(c.Contenido)
    	context = Context({"alumno": a,"N":funciones.ContarAmonestacionesAcumuladasAlumno(a.id)})

        return super(carta, self).get_context_data(
            pagesize="A4",
            title="Cartarta amonestaciones",
            content= template.render(context),
            **kwargs
        )

