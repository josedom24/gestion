# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0004_auto_20150506_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amonestaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fecha', models.DateField()),
                ('Hora', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Primera'), (b'2', b'Segunda'), (b'3', b'Tercera'), (b'4', b'Recreo'), (b'5', b'Cuarta'), (b'6', b'Quinta'), (b'7', b'Sexta')])),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(to='centro.Alumnos')),
                ('Profesor', models.ForeignKey(to='centro.Profesores')),
            ],
            options={
                'verbose_name': 'Amonestaci\xf3n',
                'verbose_name_plural': 'Amonestaciones',
            },
            bases=(models.Model,),
        ),
    ]
