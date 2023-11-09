from django import forms
from correo.models import Correos
from centro.models import Cursos,Departamentos,Areas
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

class BuscarDestinatariosForm(forms.Form):
    Profesores = forms.ChoiceField(choices=[],required=False,widget=forms.Select(attrs={'class': "form-control",'onchange': 'this.form.submit();'}))
    def __init__(self, *args, **kwargs):
            super(BuscarDestinatariosForm, self).__init__(*args, **kwargs)
            lista=["Ninguno","Todos","ETCP","Bilingüe","Consejo Escolar"]
            #Tutores
            for i in Cursos.objects.all().order_by("Curso"):
                lista.append("Tutoria: "+i.Curso)
            #Equipo Eduactivos:

            for i in Cursos.objects.all().order_by("Curso"):
                lista.append("Equipo Educativo: "+i.Curso)
            #Departamentos

            for i in Departamentos.objects.all().order_by("Nombre"):
                lista.append("Departamento: "+i.Nombre)
            #Areas

            for i in Areas.objects.all().order_by("Nombre"):
                lista.append("Areas: "+i.Nombre)
            lista2=[]
            for i in range(0,len(lista)):
                lista2.append((i,lista[i]))
            
            self.fields['Profesores'].choices=lista2
