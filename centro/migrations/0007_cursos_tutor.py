# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0006_remove_cursos_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='Tutor',
            field=models.OneToOneField(related_name='Tutor_de', default=None, to='centro.Profesores'),
            preserve_default=True,
        ),
    ]
