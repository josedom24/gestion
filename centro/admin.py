# -*- coding: utf-8 -*-
from django.contrib import admin
from centro.models import Cursos,Alumnos

# Register your models here.
admin.site.site_header="Gonzalo Nazareno"
admin.site.index_title="Gestión amonestaciones"
admin.site.register(Cursos)
admin.site.register(Alumnos)