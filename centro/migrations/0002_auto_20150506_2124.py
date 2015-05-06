# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Ap1tutor',
            field=models.CharField(max_length=20, verbose_name=b'Apellido 1 Tutor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Ap2tutor',
            field=models.CharField(max_length=20, verbose_name=b'Apellido 2 Tutor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Nomtutor',
            field=models.CharField(max_length=20, verbose_name=b'Nombre Tutor'),
            preserve_default=True,
        ),
    ]
