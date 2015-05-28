# -*- coding: utf-8 -*-
from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from impresora.models import Carta
from django.template import Context, Template, loader
from centro.models import Alumnos
from convivencia.models import Amonestaciones,Citaciones,Sanciones
from funciones import funciones
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from django.http import HttpResponse



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
      
        #sancion=Sanciones.objects.filter(Fecha=fecha)
        sancion=Alumnos.objects.all()[:45]
        #anchura=["20%","20%","30%","10%","10%","10%"]
        #kwargs["header"]=zip(anchura,['Nombre','Unidad','Sancion','Fecha ini','Fecha fin','Fecha inc'])
        contenido=""
        listado=[]
        cont=1
        t = loader.get_template('impresora/listado_sanciones.html')
        for alum in sancion:
            listado.append(alum)
            if cont % 4 ==0:
             
                anchura=["100%"]
                context = Context({"header": zip(anchura,['Nombre']),"content":listado})
                contenido=contenido+t.render(context)
                #contenido=contenido+"<div><pdf:nextpage/></div>"
                listado=[]
            cont=cont+1
        kwargs["fecha"]=fecha
        kwargs["content2"]=contenido
        return super(Listado, self).get_context_data(
            pagesize="A4 landscape",
            title="Resumen sanciones",
            #content= template.render(context),
            **kwargs
        )
  
   
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=hello.pdf'
 
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
 
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
 
    # Close the PDF object cleanly, and we're done.
    cm = 2.54
    # Create the PDF object, using the response object as its "file."
    elements = []

    doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
    data=[(1,2),(3,4)]
    table = Table(data, colWidths=270, rowHeights=79)
    elements.append(table)
    doc.build(elements) 
    p.showPage()
    p.save()
    return response
