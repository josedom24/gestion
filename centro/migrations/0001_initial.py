from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('DNI', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=60)),
                ('CodPostal', models.CharField(max_length=5, verbose_name='C\xf3digo postal')),
                ('Localidad', models.CharField(max_length=30)),
                ('Fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Provincia', models.CharField(max_length=30)),
                ('Ap1tutor', models.CharField(max_length=20, verbose_name='Apellido 1 Tutor')),
                ('Ap2tutor', models.CharField(max_length=20, verbose_name='Apellido 2 Tutor')),
                ('Nomtutor', models.CharField(max_length=20, verbose_name='Nombre tutor')),
                ('Telefono1', models.CharField(blank=True, max_length=12)),
                ('Telefono2', models.CharField(blank=True, max_length=12)),
                ('Obs', models.TextField(blank=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Abr', models.CharField(max_length=4)),
                ('Nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Telefono', models.CharField(blank=True, max_length=9)),
                ('Movil', models.CharField(blank=True, max_length=9)),
                ('Email', models.EmailField(max_length=254)),
                ('Baja', models.BooleanField(default=False)),
                ('Ce', models.BooleanField(default=False, verbose_name='Consejo Escolar')),
                ('Etcp', models.BooleanField(default=False)),
                ('Tic', models.BooleanField(default=False)),
                ('Bil', models.BooleanField(default=False, verbose_name='Biling\xfce')),
                ('Departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centro.Departamentos')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='cursos',
            name='Tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tutor_de', to='centro.Profesores'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='Unidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centro.Cursos'),
        ),
    ]
