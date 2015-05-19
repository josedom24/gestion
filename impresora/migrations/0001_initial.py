# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo', models.CharField(max_length=30, verbose_name=b'T\xc3\xadtulo')),
                ('Contenido', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Carta',
                'verbose_name_plural': 'Cartas',
            },
            bases=(models.Model,),
        ),
    ]
