# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clasedocumento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='registro',
            options={'verbose_name': 'Registro', 'verbose_name_plural': 'Registros'},
        ),
    ]
