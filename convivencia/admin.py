from django.contrib import admin
from convivencia.models import Amonestaciones,FaltasLeves,FaltasGraves,Sanciones,SancionesLeves,SancionesGraves,SancionesOtras

admin.site.register(Amonestaciones)
admin.site.register(FaltasLeves)
admin.site.register(FaltasGraves)
admin.site.register(Sanciones)
admin.site.register(SancionesLeves)
admin.site.register(SancionesGraves)
admin.site.register(SancionesOtras)