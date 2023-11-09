from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0003_auto_20161102_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='EquipoEducativo',
            field=models.ManyToManyField(blank=True, to='centro.Profesores', verbose_name='Equipo Educativo'),
        ),
    ]
