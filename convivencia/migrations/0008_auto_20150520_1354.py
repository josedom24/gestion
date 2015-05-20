# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0007_citaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanciones',
            name='Fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 13, 54, 9, 485138, tzinfo=utc), verbose_name=b'Fecha incorporaci\xc3\xb3n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sanciones',
            name='Sancion',
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
