# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0005_auto_20150506_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='Tutor',
        ),
    ]
