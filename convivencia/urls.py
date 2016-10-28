from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<tipo>[a-z]+)/(?P<alum_id>[0-9]+)$', views.parte),
	

]