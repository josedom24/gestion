from django import forms
from centro.models import Cursos,Departamentos

class UnidadForm(forms.Form):
	Unidad = forms.ModelChoiceField(queryset=Cursos.objects.order_by('Curso'), empty_label=None)

class DepartamentosForm(forms.Form):
	Departamento = forms.ModelChoiceField(queryset=Departamentos.objects.order_by('Nombre'), required=False)
