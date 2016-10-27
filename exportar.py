# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")
django.setup()
from centro.models import *

Cursos.objects.all().delete()
Alumnos.objects.all().delete()


file=open("datos/departamentos.txt","r")
lineas=file.readlines()
for linea in lineas:
	print linea
	lista=linea.split(",")
	d=Departamentos(Abr=lista[0],Nombre=lista[1])
	d.save()

file=open("datos/profesores.txt","r")
lineas=file.readlines()
for linea in lineas:
	print linea
	lista=linea.split(",")
	p=Profesores(Departamento=Departamentos.objects.all()[0],Nombre=lista[0],Apellidos=lista[1],Telefono=lista[2],Movil=lista[3],Email=lista[4])
	p.save()





cursos=[]
file=open("datos/alumnos.txt","r")
lineas=file.readlines()
for linea in lineas:
	lista=linea.split("|")
	cursos.append(lista[7].strip())

cursos=list(set(cursos))
cursos.sort()
cursos.pop(0)


cont=0
for c in cursos:
	print c
	c=Cursos(Curso=c,Tutor=Profesores.objects.all()[cont])
	cont=cont+1
	c.save()


#Alumnos
campos=["Nombre","DNI","Direccion","CodPostal","Localidad","Fecha_nacimiento","Provincia","Unidad","Ap1tutor","Ap2tutor","Nomtutor","Telefono1","Telefono2"]

datos=[]

for linea in lineas:
	lista=linea.split("|")
	dato={}
	for c,v in zip(campos,lista):
		unidad=True
		if c=="Fecha_nacimiento":
			v=v.split("/")
			dato[c]=v[2].strip()+"-"+v[1].strip()+"-"+v[0].strip()
		elif c=="Unidad":
			try:
				print "ini "+v
				
				dato[c]=Cursos.objects.filter(Curso=v.strip())[0]
				
			except:
				unidad=False
				print "aaaaa¡   "+v
		else:
			dato[c]=v.strip()

	if unidad:
		datos.append(dato)
	#print dato
for d in datos:
	print d
	a=Alumnos(**d)
	try:
		a.save()
	except:
		pass