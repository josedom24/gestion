from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0007_alumnos_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesores',
            options={'ordering': ('Apellidos',), 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
    ]
