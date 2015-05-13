# -*- coding: utf-8 -*-
import MySQLdb
bd = MySQLdb.connect("192.168.0.14","root","asdasd","iesgn" )
cursor = bd.cursor()
cursor.execute("select * from Registro")
resultados = cursor.fetchall()
for r in resultados:
	print r[0]+"---"+str(r[1])+"---"+str(r[2])+"---"+str(r[3])+"---"+str(r[4])+"---"+str(r[5])+"---"+str(r[6])+"---"+r[7]


#	In [97]: ddd=Registro.objects.all()   #

#	In [98]: for d in ddd:                             
#	    d.delete()
#	   ....:     #

#	In [99]: f=open("../../Descargas/registro.txt","r")#

#	In [100]: l=f.readlines()#

#	In [101]: for ll in l:
#	    datos=ll.split("---")
#	    s=Registro()
#	    s.Curso=datos[0]
#	    s.Fecha=datos[1]
#	    s.N=datos[2]
#	    s.Tipo=datos[3]
#	    s.Idp_id=datos[4]
#	    s.Idr_id=datos[5]
#	    s.Idc_id=datos[6]
#	    s.Contenido=datos[7]
#	    s.id=cont
#	    s.save()
#	    cont=cont+1
