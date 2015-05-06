# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('DNI', models.CharField(max_length=9)),
                ('Direccion', models.CharField(max_length=60)),
                ('CodPostal', models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo postal')),
                ('Localidad', models.CharField(max_length=30)),
                ('Fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('Provincia', models.CharField(max_length=30)),
                ('Ap1tutor', models.CharField(max_length=20, verbose_name=b'Apellido 1 tutor')),
                ('Ap2tutor', models.CharField(max_length=20, verbose_name=b'Apellido 2 tutor')),
                ('Nomtutor', models.CharField(max_length=20, verbose_name=b'Nombre tutor')),
                ('Telefono1', models.CharField(max_length=12, blank=True)),
                ('Telefono2', models.CharField(max_length=12, blank=True)),
                ('Obs', models.TextField(verbose_name=b'Observaciones', blank=True)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Curso', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='Unidad',
            field=models.ForeignKey(to='centro.Cursos'),
            preserve_default=True,
        ),
    ]
