from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^partes/(?P<curso>[0-9]+)$', views.imprimir_partes),
	url(r'^faltas/(?P<curso>[0-9]+)$', views.imprimir_faltas),
	url(r'^telefono/(?P<curso>[0-9]+)$', views.imprimir_telefonos),
	url(r'^historial/(?P<alum_id>[0-9]+)/(?P<prof>[a-z]*)$', views.imprimir_historial),
	url(r'^show/(?P<tipo>[a-z]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.imprimir_show),
	url(r'^send/amonestacion/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.send_amonestacion),
	url(r'^carta_amonestacion/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)/(?P<todos>[a-z]+)$', views.carta_amonestacion),
	url(r'^carta_sancion/(?P<identificador>[0-9]+)$', views.carta_sancion),
        url(r'^profesores$', views.imprimir_profesores),
        url(r'^claustro$', views.imprimir_profesores),
        url(r'^claustro/(?P<curso>[0-9]+)$', views.imprimir_profesores),
		url(r'^semana$', views.imprimir_profesores),
        url(r'^registro/(?P<tipo>[\w-])/(?P<curso>\d{4}-\d{4})$', views.imprimir_registro),
        url(r'^sanciones/hoy$', views.imprimir_sanciones_hoy),
        
]
