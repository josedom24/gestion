# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0004_auto_20150506_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='Tutor',
            field=models.OneToOneField(related_name='Tutor_de', default=None, to='centro.Profesores'),
            preserve_default=True,
        ),
    ]
