from django.contrib import admin
from absentismo.models import Actuaciones, TiposActuaciones

# Register your models here.
class ActuacionesAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    list_filter = ['Fecha', 'IdAlumno']
    list_display = ['Fecha', 'IdAlumno', 'unidad', 'Tipo', 'Comentario']

    def unidad(self, obj):
        return obj.IdAlumno.Unidad

    unidad.admin_order_field = 'IdAlumno__unidad'

    search_fields = ['Comentario']


admin.site.register(TiposActuaciones)
admin.site.register(Actuaciones, ActuacionesAdmin)