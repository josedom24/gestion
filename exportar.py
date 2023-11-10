# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")
django.setup()
from centro.models import *
from registro.models import *
from convivencia.models import *
import os
import csv
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)#




Amonestaciones.objects.all().delete()
Sanciones.objects.all().delete()


with open('datos/datos/Partes.csv', 'rb') as mycsvfile:
    dictofdata = csv.DictReader(mycsvfile, dialect='mydialect')
    for row in dictofdata:
    	print row
    	row["id"]=row["Id"]
    	del row["Id"]
    	row["IdAlumno"]=Alumnos.objects.get(id=row["Ida"])
    	
    	del row["Ida"]
    	if row["Tipo"]=="a":
    		del row["Tipo"]
	    	
	    	
    		
    		if row["Id_prof"]=="-1":
    			row["Profesor"]=Profesores.objects.get(id=147)
    		else:
    			row["Profesor"]=Profesores.objects.get(id=row["Id_prof"])
    		
    		del row["Sancion"]
    		del row["Fecha_fin"]
    		del row["Id_prof"]
    		
    		a=Amonestaciones(**row)
    		a.save()
    	else:
    		del row["Tipo"]
    		del row["Hora"]
    		del row["Id_prof"]
    		a=Sanciones(**row)
    		a.save()

