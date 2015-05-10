from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^amonestacion/(?P<alum_id>[0-9]+)$', views.amonestacion),
    #url(r'^$', views.index, name='index'),

]