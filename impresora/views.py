from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from impresora.models import Carta
from django.template import Context, Template, loader
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Citaciones,Sanciones
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

class CartaSancion(PDFTemplateView):
    template_name = "impresora/carta.html"
    

    def get_context_data(self, **kwargs):
        idsancion=int(self.kwargs['sancion'])
        c=Carta.objects.get(Titulo="Sancion")
        sancion=Sanciones.objects.get(id=idsancion)
        alum=Alumnos.objects.get(id=sancion.IdAlumno_id)
        template = Template(c.Contenido)
        context = Context({"alumno": alum,"sancion":sancion,"fecha":datetime.now()})
            

            

        return super(CartaSancion, self).get_context_data(
            pagesize="A4",
            title="Carta citaciones",
            content= template.render(context),
            **kwargs
        )

class Listado(PDFTemplateView):
    template_name = "impresora/listado.html"
    

    def get_context_data(self, **kwargs):
        fecha=datetime(2015,5,13)
        
        sancion=Sanciones.objects.filter(Fecha=fecha)
        template = loader.get_template('impresora/listado.html')
        #anchura=["20%","20%","30%","10%","10%","10%"]
        #kwargs["header"]=zip(anchura,['Nombre','Unidad','Sancion','Fecha ini','Fecha fin','Fecha inc'])
        anchura=["100%"]
        kwargs["header"]=zip(anchura,['Nombre'])
        kwargs["content"]=sancion
        kwargs["fecha"]=fecha
            

        return super(Listado, self).get_context_data(
            pagesize="A4 landscape",
            title="Resumen sitaciones",
            #content= template.render(context),
            **kwargs
        )