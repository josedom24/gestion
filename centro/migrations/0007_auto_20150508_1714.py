# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0006_auto_20150508_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='Profesores',
            field=models.ManyToManyField(to='centro.Profesores', blank=True),
            preserve_default=True,
        ),
    ]
