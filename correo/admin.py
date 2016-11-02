from django.contrib import admin
from correo.models import Correos
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
class CorreosAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Fecha']
    list_display = ["Fecha",'Asunto']
     
    search_fields = ['Asunto','Contenido']

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Profesores", is_stacked=False)},
    }
   

# Register your models here.
admin.site.register(Correos,CorreosAdmin)