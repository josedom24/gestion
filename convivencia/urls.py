from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^amonestacion/(?P<alum_id>[0-9]+)$', views.amonestacion),
	url(r'^sancion/(?P<alum_id>[0-9]+)$', views.sancion),
	url(r'^citacion/(?P<alum_id>[0-9]+)$', views.citacion),
	url(r'^historial/(?P<alum_id>[0-9]+)$', views.historial),
	url(r'^resumen/(?P<tipo>[\w-])/$', views.resumen_hoy),
	url(r'^resumen/(?P<tipo>[\w-])/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)$', views.resumen),
	url(r'^show/(?P<tipo>[\w-])/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)/(?P<dia>[0-9]+)$', views.show),
    #url(r'^$', views.index, name='index'),

]