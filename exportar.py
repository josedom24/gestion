# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")
django.setup()
from centro.models import *
from registro.models import *
import os
#Procedencia.objects.all().delete()
#file=open("datos/procedencia.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	print linea
#	lista=linea.split(",")
#	d=Procedencia(id=lista[0],Procedencia=lista[1])
#	d.save()


#Remitente.objects.all().delete()
#file=open("datos/remitente.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	print linea
#	lista=linea.split(",")
#	d=Remitente(id=lista[0],Remitente=lista[1])
#	d.save()

#ClaseDocumento.objects.all().delete()
#file=open("datos/documentos.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	print linea
#	lista=linea.split(",")
#	d=ClaseDocumento(id=lista[0],ClaseDocumento=lista[1])
#	d.save()
Registro.objects.all().delete()
campos=["Curso","Fecha","N","Tipo","Idp","Idr","Idc","Contenido"]


file=open("datos/registro.txt","r")

linea=file.readlines()[0]
lista=linea.split("),(")
for linea in lista:
	dato={}	
	lista2=linea.split(",")
	for c,v in zip(campos,lista2):
	
		if c=="Idp":
			try:
				dato[c]=Procedencia.objects.filter(id=v.strip())[0]
			except:
				dato[c]=None
		elif c=="Idr":
			try:
				dato[c]=Remitente.objects.filter(id=v.strip())[0]
			except:
				dato[c]=None
		elif c=="Idc":
			try:
				dato[c]=ClaseDocumento.objects.filter(id=v.strip())[0]
			except:
				dato[c]=None
		elif c=="Fecha":
			try:
				dato[c]=v.strip()[1:-1]
			except:
				pass
		else:
			dato[c]="%s"% v.strip().decode("utf8")
		
	#print dato
	#a=Registro(**dato)
	#a.save()
	



#Cursos.objects.all().delete()
#Alumnos.objects.all().delete()#
#

#file=open("datos/departamentos.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	print linea
#	lista=linea.split(",")
#	d=Departamentos(Abr=lista[0],Nombre=lista[1])
#	d.save()#

#file=open("datos/profesores.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	print linea
#	lista=linea.split(",")
#	p=Profesores(Departamento=Departamentos.objects.all()[0],Nombre=lista[0],Apellidos=lista[1],Telefono=lista[2],Movil=lista[3],Email=lista[4])
#	p.save()#
#
#
#
#

#cursos=[]
#file=open("datos/alumnos.txt","r")
#lineas=file.readlines()
#for linea in lineas:
#	lista=linea.split("|")
#	cursos.append(lista[7].strip())#

#cursos=list(set(cursos))
#cursos.sort()
#cursos.pop(0)#
#

#cont=0
#for c in cursos:
#	print c
#	c=Cursos(Curso=c,Tutor=Profesores.objects.all()[cont])
#	cont=cont+1
#	c.save()#
#

##Alumnos
#campos=["Nombre","DNI","Direccion","CodPostal","Localidad","Fecha_nacimiento","Provincia","Unidad","Ap1tutor","Ap2tutor","Nomtutor","Telefono1","Telefono2"]#

#datos=[]#

#for linea in lineas:
#	lista=linea.split("|")
#	dato={}
#	for c,v in zip(campos,lista):
#		unidad=True
#		if c=="Fecha_nacimiento":
#			v=v.split("/")
#			dato[c]=v[2].strip()+"-"+v[1].strip()+"-"+v[0].strip()
#		elif c=="Unidad":
#			try:
#				print "ini "+v
#				
#				dato[c]=Cursos.objects.filter(Curso=v.strip())[0]
#				
#			except:
#				unidad=False
#				print "aaaaa¡   "+v
#		else:
#			dato[c]=v.strip()#

#	if unidad:
#		datos.append(dato)
#	#print dato
#for d in datos:
#	print d
#	a=Alumnos(**d)
#	try:
#		a.save()
#	except:
#		pass