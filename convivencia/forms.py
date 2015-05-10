from django import forms
from django.forms import ModelForm
from convivencia.models import Amonestaciones
from django.forms.widgets import CheckboxSelectMultiple,HiddenInput,DateInput


class AmonestacionForm(forms.ModelForm):
	class Meta:
		model = Amonestaciones
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
            'FaltasLeves': CheckboxSelectMultiple(),
            'FaltasGraves': CheckboxSelectMultiple(),

        }