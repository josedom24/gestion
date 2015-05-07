from django.contrib import admin
from convivencia.models import Amonestaciones,FaltasLeves,FaltasGraves

admin.site.register(Amonestaciones)
admin.site.register(FaltasLeves)
admin.site.register(FaltasGraves)