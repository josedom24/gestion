from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amonestaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Hora', models.CharField(choices=[('1', 'Primera'), ('2', 'Segunda'), ('3', 'Tercera'), ('4', 'Recreo'), ('5', 'Cuarta'), ('6', 'Quinta'), ('7', 'Sexta')], default='1', max_length=1)),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Alumnos')),
                ('Profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Profesores')),
            ],
            options={
                'verbose_name': 'Amonestaci\xf3n',
                'verbose_name_plural': 'Amonestaciones',
            },
        ),
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Fecha_fin', models.DateField(verbose_name='Fecha finalizaci\xf3n')),
                ('Fecha_incorporacion', models.DateField(verbose_name='Fecha incorporaci\xf3n')),
                ('Sancion', models.CharField(max_length=100)),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.Alumnos')),
            ],
            options={
                'verbose_name': 'Sanci\xf3n',
                'verbose_name_plural': 'Sanciones',
            },
        ),
    ]
