from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from impresora.models import Carta
from django.template import Context, Template
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Citaciones
from funciones import funciones
from datetime import datetime

class CartaAmonestacion(PDFTemplateView):
    template_name = "impresora/carta.html"
    

    def get_context_data(self, **kwargs):
        fecha=datetime(int(self.kwargs['ano']),int(self.kwargs['mes']),int(self.kwargs['dia']))
    	c=Carta.objects.get(Titulo="Amonestacion")
        list_a=Amonestaciones.objects.filter(Fecha=fecha)
        texto=""
        for amon in list_a:
            a=Alumnos.objects.get(id=amon.IdAlumno_id)
            template = Template(c.Contenido)
            context = Context({"alumno": a,"N":funciones.ContarAmonestacionesAcumuladasAlumno(a.id)})
            texto=texto+template.render(context)
            texto=texto+"<pdf:nextpage/>"

    	    

        return super(CartaAmonestacion, self).get_context_data(
            pagesize="A4",
            title="Carta amonestaciones",
            content= texto,
            **kwargs
        )

class CartaCitacion(PDFTemplateView):
    template_name = "impresora/carta.html"
    

    def get_context_data(self, **kwargs):
        fecha=datetime(int(self.kwargs['ano']),int(self.kwargs['mes']),int(self.kwargs['dia']))
        c=Carta.objects.get(Titulo="Citacion")
        list_a=Citaciones.objects.filter(Fecha=fecha)
        texto=""
        for amon in list_a:
            a=Alumnos.objects.get(id=amon.IdAlumno_id)
            template = Template(c.Contenido)
            context = Context({"alumno": a})
            texto=texto+template.render(context)
            texto=texto+"<pdf:nextpage/>"

            

        return super(CartaCitacion, self).get_context_data(
            pagesize="A4",
            title="Carta citaciones",
            content= texto,
            **kwargs
        )

