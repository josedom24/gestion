# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0003_auto_20150507_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='amonestaciones',
            name='FaltasGrave',
            field=models.ManyToManyField(to='convivencia.FaltasGraves'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='amonestaciones',
            name='FaltasLeves',
            field=models.ManyToManyField(to='convivencia.FaltasLeves'),
            preserve_default=True,
        ),
    ]
