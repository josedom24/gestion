from django import forms
from centro.models import Cursos,Departamentos

class UnidadForm(forms.Form):
	Unidad = forms.ModelChoiceField(queryset=Cursos.objects.order_by('Curso'), empty_label=None,widget=forms.Select(attrs={'class': "form-control"}))

class DepartamentosForm(forms.Form):
	Departamento = forms.ModelChoiceField(queryset=Departamentos.objects.order_by('Nombre'), required=False,widget=forms.Select(attrs={'class': "form-control"}))
