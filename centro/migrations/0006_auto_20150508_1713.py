# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0005_altaalumnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altaalumnos',
            name='Fichero',
            field=models.FileField(upload_to=b'alta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursos',
            name='Tutor',
            field=models.OneToOneField(related_name='Tutor_de', default=None, blank=True, to='centro.Profesores'),
            preserve_default=True,
        ),
    ]
