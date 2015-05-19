# -*- coding: utf-8 -*-
from django.contrib import admin
from impresora.models import Carta
# Register your models here.

class CartaAdmin(admin.ModelAdmin):
       
    search_fields = ['Contenido']

    class Media:
        js = ('/static/js/tinymce/tinymce.min.js','/static/js/tinymce/tinymce.conf.js',)

admin.site.register(Carta,CartaAdmin)