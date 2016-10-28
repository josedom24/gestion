# -*- coding: utf-8 -*-
from django.contrib import admin
from centro.models import Cursos,Alumnos,Departamentos,Profesores
# Register your models here.
class AlumnosAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Unidad','Localidad']
    list_display = ["Nombre",'DNI','Localidad','Telefono1']
     
    search_fields = ['Nombre','DNI']

class PorfesoresAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Departamento']
    list_display = ["Nombre",'Apellidos','Email','Departamento']
     
    search_fields = ['Nombre','Apellidos']
   

    # Register your models here.
admin.site.site_header="Gonzalo Nazareno"
admin.site.index_title="Gestión amonestaciones"
admin.site.register(Cursos)
admin.site.register(Alumnos,AlumnosAdmin)
admin.site.register(Departamentos)
admin.site.register(Profesores,PorfesoresAdmin)
