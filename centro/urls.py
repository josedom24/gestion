from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^alumnos$', views.alumnos),
    url(r'^profesores$', views.profesores),
]