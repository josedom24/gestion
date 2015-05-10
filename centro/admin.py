# -*- coding: utf-8 -*-
from django.contrib import admin
from centro.models import Cursos,Alumnos,Departamentos,Profesores,AltaAlumnos



class AlumnosAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Unidad','Localidad']
    list_display = ["Nombre",'DNI','Localidad','Telefono1']
     
    search_fields = ['Nombre','DNI']
   

    # Register your models here.
admin.site.site_header="Gonzalo Nazareno"
admin.site.index_title="Gestión amonestaciones"
admin.site.register(Cursos)
admin.site.register(Alumnos,AlumnosAdmin)
admin.site.register(Departamentos)
admin.site.register(Profesores)
admin.site.register(AltaAlumnos)