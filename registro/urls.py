from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^(?P<tipo>[\w-])$', views.registro),
	url(r'^add/(?P<tipo>[\w-])/$', views.add),
]