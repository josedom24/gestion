from django.urls import re_path

from . import views

urlpatterns = [
	re_path(r'^historial/(?P<alum_id>[0-9]+)/(?P<prof>[a-z]*)$', views.historial),
	re_path(r'^(?P<tipo>[a-z]+)/(?P<alum_id>[0-9]+)$', views.parte),
    re_path(r'^resumen/(?P<tipo>[a-z]+)$', views.resumen_hoy),
	re_path(r'^resumen/(?P<tipo>[a-z]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)$', views.resumen),
	re_path(r'^show/(?P<tipo>[a-z]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.show),
	re_path(r'^estadistica$', views.estadisticas),
	re_path(r'^estadistica/curso/(?P<curso>[0-9]+)$', views.estadisticas2),
	re_path(r'^grupos', views.grupos),
	re_path(r'^alumnos', views.alumnos),
	re_path(r'^horas$', views.horas),
    re_path(r'^profesores$', views.profesores),
        	

	

]
