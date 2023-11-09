
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0002_cursos_equipoeducativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='EquipoEducativo',
            field=models.ManyToManyField(blank=True, null=True, to='centro.Profesores', verbose_name='Equipo Educativo'),
        ),
    ]
