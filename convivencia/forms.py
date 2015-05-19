# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from convivencia.models import Amonestaciones,FaltasGraves,FaltasLeves,Sanciones,SancionesOtras,SancionesLeves,SancionesGraves,Citaciones
from django.forms.widgets import CheckboxSelectMultiple,HiddenInput,DateInput,Textarea
from tinymce.widgets import TinyMCE



class AmonestacionForm(forms.ModelForm):
	class Meta:
		model = Amonestaciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			#'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			'Comentario': TinyMCE(),
            'FaltasLeves': CheckboxSelectMultiple(choices=FaltasLeves.objects.order_by('id')),
            'FaltasGraves': CheckboxSelectMultiple(choices=FaltasGraves.objects.order_by('id')),

        }

class SancionForm(forms.ModelForm):
	class Meta:
		model = Sanciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			'Fecha_fin':DateInput(),
			#'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			'Comentario': TinyMCE(),
            'SancionesLeves': CheckboxSelectMultiple(choices=SancionesLeves.objects.order_by('id')),
            'SancionesGraves': CheckboxSelectMultiple(choices=SancionesGraves.objects.order_by('id')),
            'SancionesOtras': CheckboxSelectMultiple(choices=SancionesOtras.objects.order_by('id')),

        }

class TipoResumen(forms.Form):
	CHOICES=[('a','Amonestación'),('s','Sanción'),('c','Citación')]
	tipo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class CitacionForm(forms.ModelForm):
	class Meta:
		model = Citaciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			#'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),ç
			'Comentario': TinyMCE(),
            

        }