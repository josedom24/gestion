# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
from django.forms.widgets import HiddenInput,DateInput,Textarea,TextInput,Select

class RegistroForm(forms.ModelForm):
	Idp	= forms.ModelChoiceField(required=True,queryset=Procedencia.objects.all(),empty_label="",label="Procedencia")
	Idr= forms.ModelChoiceField(required=True,queryset=Remitente.objects.all(), empty_label="",label="Remitente")
	Idc= forms.ModelChoiceField(required=True,queryset=ClaseDocumento.objects.all(), empty_label="",label="Documento")
	class Meta:
		model = Registro
		fields = "__all__"
		labels = {
            'Idp': ('Procedencia'),
        }
		widgets = {
			'Curso':HiddenInput(),
			'N':HiddenInput(),
			'Tipo':HiddenInput(),
			'Fecha':DateInput(),
			'Contenido': Textarea(attrs={'cols': 90, 'rows': 15}),
			
			
			
            

        }
class BuscarRegistroForm(forms.Form):
	Hasta=forms.DateField(required=False)
	Desde=forms.DateField(required=False)
	Procedencia= forms.ModelChoiceField(required=False,queryset=Procedencia.objects.all(),empty_label="")
	Remitente= forms.ModelChoiceField(required=False,queryset=Remitente.objects.all(), empty_label="")
	Documento= forms.ModelChoiceField(required=False,queryset=ClaseDocumento.objects.all(), empty_label="")
	Contenido=forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '40'}))
	
