# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0003_auto_20161028_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposAmonestaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoAmonestacion', models.CharField(max_length=60)),
            ],
        ),
    ]
