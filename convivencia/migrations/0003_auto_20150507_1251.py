# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0002_auto_20150507_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amonestaciones',
            name='FaltasGrave',
        ),
        migrations.RemoveField(
            model_name='amonestaciones',
            name='FaltasLeves',
        ),
    ]
