from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^list$', views.list_correo),
    re_path(r'^new$', views.new_correo),
]
