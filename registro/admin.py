from django.contrib import admin

from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
# Register your models here.
class RegistroAdmin(admin.ModelAdmin):
    date_hierarchy = 'Fecha'
    actions_selection_counter=False
    list_filter = ['Tipo','Curso']
      
    search_fields = ['Contenido']

    #class Media:
    #    js = ('/static/js/tinymce/tinymce.min.js','/static/js/tinymce/tinymce.conf.js',)

admin.site.register(Procedencia)
admin.site.register(Remitente)
admin.site.register(ClaseDocumento)
admin.site.register(Registro,RegistroAdmin)