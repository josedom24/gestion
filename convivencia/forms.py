from django import forms
from django.forms import ModelForm,ModelChoiceField
from convivencia.models import Amonestaciones,Sanciones
from centro.models import Profesores
from django.forms.widgets import CheckboxSelectMultiple,HiddenInput,DateInput,Textarea,TextInput,Select


class AmonestacionForm(forms.ModelForm):
	Profesor = ModelChoiceField(Profesores.objects.all().order_by("Apellidos"), empty_label=None)
	class Meta:
		model = Amonestaciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			
			#'Comentario': TinyMCE(),

        }

class SancionForm(forms.ModelForm):
	class Meta:
		model = Sanciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':DateInput(),
			'Fecha_fin':DateInput(),
			
			'Sancion':TextInput(attrs={'size': '67'}),
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			#'Comentario': TinyMCE(),
            
        }