# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from registro.models import Procedencia,Remitente,ClaseDocumento,Registro
from django.forms.widgets import HiddenInput,DateInput,Textarea,TextInput,Select,SelectDateWidget
from datetime import datetime

class RegistroForm(forms.ModelForm):
	Idp	= forms.ModelChoiceField(queryset=Procedencia.objects.all().order_by("Procedencia"),empty_label=None,label="Procedencia",widget=forms.Select(attrs={'class': "form-control"}))
	Idr= forms.ModelChoiceField(queryset=Remitente.objects.all().order_by("Remitente"), empty_label=None,label="Remitente",widget=forms.Select(attrs={'class': "form-control"}))
	Idc= forms.ModelChoiceField(queryset=ClaseDocumento.objects.all().order_by("ClaseDocumento"), empty_label=None,label="Documento",widget=forms.Select(attrs={'class': "form-control"}))
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
			'Fecha':SelectDateWidget(),
        		'Contenido': Textarea(attrs={'cols': 95, 'rows': 15}),
	                 }
        def __init__(self, *args, **kwargs):
		super(RegistroForm, self).__init__(*args, **kwargs)
                if args[0]["Tipo"]=="s":
                    self.fields["Idp"].label="Destino"
                    self.fields["Idr"].label="Destinatario"
		
class BuscarRegistroForm(forms.Form):
	Hasta=forms.DateField(required=False,widget=SelectDateWidget())
	Desde=forms.DateField(required=False,widget=SelectDateWidget())
	Curso= forms.ChoiceField(choices=(),widget=forms.Select(attrs={'class': "form-control"}))
	Procedencia= forms.ModelChoiceField(required=False,queryset=Procedencia.objects.all().order_by("Procedencia"),empty_label="",widget=forms.Select(attrs={'class': "form-control"}))

	Remitente= forms.ModelChoiceField(required=False,queryset=Remitente.objects.all().order_by("Remitente"), empty_label="",widget=forms.Select(attrs={'class': "form-control"}))
	Documento= forms.ModelChoiceField(required=False,queryset=ClaseDocumento.objects.all().order_by("ClaseDocumento"), empty_label="",widget=forms.Select(attrs={'class': "form-control"}))
	Contenido=forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '40'}))
	def __init__(self, *args, **kwargs):
		super(BuscarRegistroForm, self).__init__(*args, **kwargs)
		choices = [(pt, pt) for pt in Registro.objects.values("Curso").distinct().values_list("Curso", flat=True).distinct()]
		#choices.extend(EXTRA_CHOICES)
		
		hoy=datetime.now()
		if hoy.month>=9:
			choices.append((str(hoy.year)+"-"+str(hoy.year+1),str(hoy.year)+"-"+str(hoy.year+1)))
			self.fields['Curso'].choices = choices
			self.fields['Curso'].initial=str(hoy.year)+"-"+str(hoy.year+1)
		else:
			self.fields['Curso'].choices = choices
			self.fields['Curso'].initial=str(hoy.year-1)+'-'+str(hoy.year)
