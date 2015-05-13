# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ClaseDocumento', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Docuemnto',
                'verbose_name_plural': 'Docuemntos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Procedencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Procedencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Procedencia',
                'verbose_name_plural': 'Procedencias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Curso', models.CharField(max_length=9)),
                ('Fecha', models.DateField()),
                ('N', models.IntegerField()),
                ('Tipo', models.CharField(max_length=7)),
                ('Contenido', models.TextField(blank=True)),
                ('Idc', models.ForeignKey(to='registro.ClaseDocumento')),
                ('Idp', models.ForeignKey(to='registro.Procedencia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remitente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Remitente', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Temitente',
                'verbose_name_plural': 'Remitentes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='registro',
            name='Idr',
            field=models.ForeignKey(to='registro.Remitente'),
            preserve_default=True,
        ),
    ]
