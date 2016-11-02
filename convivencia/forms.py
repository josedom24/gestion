from django import forms
from django.forms import ModelForm,ModelChoiceField
from convivencia.models import Amonestaciones,Sanciones
from centro.models import Profesores
from django.forms.widgets import CheckboxSelectMultiple,HiddenInput,DateInput,Textarea,TextInput,Select,SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget 



class AmonestacionForm(forms.ModelForm):
	Profesor = ModelChoiceField(Profesores.objects.all().order_by("Apellidos"), empty_label=None)
	class Meta:
		model = Amonestaciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':SelectDateWidget(),
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			
			#'Comentario': TinyMCE(),

        }

class SancionForm(forms.ModelForm):
	class Meta:
		model = Sanciones
		fields = "__all__"
		widgets = {
			'IdAlumno':HiddenInput(),
			'Fecha':SelectDateWidget(),
			'Fecha_fin':SelectDateWidget(),
			
			'Sancion':TextInput(attrs={'size': '67'}),
			'Comentario': Textarea(attrs={'cols': 90, 'rows': 15}),
			#'Comentario': TinyMCE(),
            
        }