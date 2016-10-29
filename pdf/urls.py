from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^partes/(?P<curso>[0-9]+)$', views.imprimir_partes),
	
]