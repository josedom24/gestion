from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^logout/$', views.logout_view),
	url(r'^alta/$', views.alta),
    url(r'^$', views.index, name='index'),

]