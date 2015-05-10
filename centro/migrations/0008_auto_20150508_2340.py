# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0007_auto_20150508_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='DNI',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
