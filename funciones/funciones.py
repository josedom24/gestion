from convivencia.models import Amonestaciones,Sanciones,Citaciones
from datetime import datetime
def ContarFaltas(lista_id):
	contar=[]
	for alum in lista_id:

		am=str(len(Amonestaciones.objects.filter(IdAlumno_id=alum.values()[0])))
		sa=str(len(Sanciones.objects.filter(IdAlumno_id=alum.values()[0])))
		ci=str(len(Citaciones.objects.filter(IdAlumno_id=alum.values()[0])))
		contar.append(am+"/"+sa+"/"+ci)
	return contar

def ContarAmonestacionesAcumuladasAlumno(id):
	
	sa=Sanciones.objects.filter(IdAlumno_id=id).order_by('Fecha').last()
	if sa:
		am=Amonestaciones.objects.filter(IdAlumno_id=id).filter(Fecha__gte=sa.Fecha)
		return(str(len(am)))
	else:
		return("0")

def ContarAmonestacionesAcumuladas(lista_id):
	contar=[]
	for alum in lista_id:	
		contar.append(ContarAmonestacionesAcumuladasAlumno(alum.values()[0]))
	return contar

def AddMonths(d,x):
    newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    newyear  = d.year + ((( d.month - 1) + x ) / 12 ) 
    return datetime( newyear, newmonth, d.day)