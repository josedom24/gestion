# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0003_profesores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='Tutor',
        ),
        migrations.AddField(
            model_name='cursos',
            name='Profesores',
            field=models.ManyToManyField(to='centro.Profesores'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursos',
            name='Tutor',
            field=models.OneToOneField(related_name='Tutor_de', default=None, to='centro.Profesores'),
            preserve_default=True,
        ),
    ]
