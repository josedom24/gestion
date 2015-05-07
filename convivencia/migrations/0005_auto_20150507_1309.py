# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0004_auto_20150506_2253'),
        ('convivencia', '0004_auto_20150507_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fecha', models.DateField()),
                ('Fecha_fin', models.DateField(verbose_name=b'Fecha finalizaci\xc3\xb3n')),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(to='centro.Alumnos')),
            ],
            options={
                'verbose_name': 'Sanci\xf3n',
                'verbose_name_plural': 'Sanciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SancionesGraves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sancion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sanci\xf3n Grave',
                'verbose_name_plural': 'Sanciones Graves',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SancionesLeves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sancion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sanci\xf3n Leve',
                'verbose_name_plural': 'Sanciones Leves',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SancionesOtras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sancion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Otra Sanci\xf3n',
                'verbose_name_plural': 'Otras Sanciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sanciones',
            name='SancionesGraves',
            field=models.ManyToManyField(to='convivencia.SancionesGraves', verbose_name=b'Sanciones Graves'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanciones',
            name='SancionesLeves',
            field=models.ManyToManyField(to='convivencia.SancionesLeves', verbose_name=b'Sanciones Leves'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanciones',
            name='SancionesOtras',
            field=models.ManyToManyField(to='convivencia.SancionesOtras', verbose_name=b'Otras Sanciones'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='amonestaciones',
            name='FaltasGrave',
        ),
        migrations.AddField(
            model_name='amonestaciones',
            name='FaltasGraves',
            field=models.ManyToManyField(to='convivencia.FaltasGraves', verbose_name=b'Faltas Graves'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amonestaciones',
            name='FaltasLeves',
            field=models.ManyToManyField(to='convivencia.FaltasLeves', verbose_name=b'Faltas Leves'),
            preserve_default=True,
        ),
    ]
