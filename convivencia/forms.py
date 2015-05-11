from django import forms
from django.forms import ModelForm
from convivencia.models import Amonestaciones,FaltasGraves,FaltasLeves,Sanciones,SancionesOtras,SancionesLeves,SancionesGraves
from django.forms.widgets import CheckboxSelectMultiple,HiddenInput,DateInput,Textarea


class AmonestacionForm(forms.ModelForm):
	class Meta:
		model = Amonestaciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
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
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
            'SancionesLeves': CheckboxSelectMultiple(choices=SancionesLeves.objects.order_by('id')),
            'SancionesGraves': CheckboxSelectMultiple(choices=SancionesGraves.objects.order_by('id')),
            'SancionesOtras': CheckboxSelectMultiple(choices=SancionesOtras.objects.order_by('id')),

        }