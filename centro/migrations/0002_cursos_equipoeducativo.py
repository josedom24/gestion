from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='EquipoEducativo',
            field=models.ManyToManyField(to='centro.Profesores', verbose_name='Equipo Educativo'),
        ),
    ]
