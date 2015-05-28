from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^carta/amonestaciones/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', login_required(views.CartaAmonestacion.as_view())),
	url(r'^carta/citaciones/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', login_required(views.CartaCitacion.as_view())),
	url(r'^carta/sanciones/(?P<sancion>[0-9]+)$', login_required(views.CartaSancion.as_view())),
	url(r'^listado$', login_required(views.Listado.as_view())),
	url(r'^listado2$', login_required(views.hello_pdf)),
	
]