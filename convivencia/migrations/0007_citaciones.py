# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0008_auto_20150508_2340'),
        ('convivencia', '0006_auto_20150511_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fecha', models.DateField()),
                ('Comentario', models.TextField(blank=True)),
                ('IdAlumno', models.ForeignKey(to='centro.Alumnos')),
            ],
            options={
                'verbose_name': 'Citaci\xf3n',
                'verbose_name_plural': 'Citaciones',
            },
            bases=(models.Model,),
        ),
    ]
