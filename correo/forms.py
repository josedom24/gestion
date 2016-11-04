from django import forms
from django.forms import ModelForm
from correo.models import Correos
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import HiddenInput,Textarea,TextInput
class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correos
        fields = "__all__"
        widgets = {
                 'Fecha':HiddenInput(),
                 'Asunto': TextInput(attrs={'size':80}),
                 'Destinatarios': FilteredSelectMultiple("Profesores", is_stacked=False),
                 'Contenido': Textarea(attrs={'cols': 100, 'rows': 15}),
                 }
    class Media:
        css = {'all':('admin/css/widgets.css','css/overrides.css'),}
        js = ('admin/js/vendor/jquery/jquery.js','/admin/jsi18n/','admin/js/jquery.init.js')
