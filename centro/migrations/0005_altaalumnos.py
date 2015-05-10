# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0004_auto_20150506_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltaAlumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fichero', models.FileField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'Alta Alumnos',
                'verbose_name_plural': 'Alta Alumnos',
            },
            bases=(models.Model,),
        ),
    ]
