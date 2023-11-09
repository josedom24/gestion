from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^(?P<tipo>[\w-])$', views.registro),
	re_path(r'^add/(?P<tipo>[\w-])$', views.add),
]