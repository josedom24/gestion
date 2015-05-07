# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaltasGraves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Falta', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Falta Grave',
                'verbose_name_plural': 'Faltas Graves',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FaltasLeves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Falta', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Falta Leve',
                'verbose_name_plural': 'Faltas Leves',
            },
            bases=(models.Model,),
        ),
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
