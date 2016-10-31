# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
from django.forms.widgets import HiddenInput,DateInput,Textarea,TextInput,Select
from datetime import datetime

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
	Curso= forms.ChoiceField(choices=(),widget=forms.Select(attrs={'class': "form-control"}))
	Procedencia= forms.ModelChoiceField(required=False,queryset=Procedencia.objects.all(),empty_label="",widget=forms.Select(attrs={'class': "form-control"}))

	Remitente= forms.ModelChoiceField(required=False,queryset=Remitente.objects.all(), empty_label="",widget=forms.Select(attrs={'class': "form-control"}))
	Documento= forms.ModelChoiceField(required=False,queryset=ClaseDocumento.objects.all(), empty_label="",widget=forms.Select(attrs={'class': "form-control"}))
	Contenido=forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '40'}))

	def __init__(self, *args, **kwargs):
		super(BuscarRegistroForm, self).__init__(*args, **kwargs)
		choices = [(pt, pt) for pt in Registro.objects.values("Curso").distinct().values_list("Curso", flat=True).distinct()]
		#choices.extend(EXTRA_CHOICES)
		self.fields['Curso'].choices = choices
		hoy=datetime.now()
		if hoy.month>=9:
			self.fields['Curso'].initial=str(hoy.year)+"-"+str(hoy.year+1)
		else:
			self.fields['Curso'].initial=str(hoy.year-1)+'-'+str(hoy.year)
		