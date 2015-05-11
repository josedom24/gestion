# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0005_auto_20150507_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amonestaciones',
            name='FaltasGraves',
            field=models.ManyToManyField(to='convivencia.FaltasGraves', verbose_name=b'Faltas Graves', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amonestaciones',
            name='FaltasLeves',
            field=models.ManyToManyField(to='convivencia.FaltasLeves', verbose_name=b'Faltas Leves', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanciones',
            name='SancionesGraves',
            field=models.ManyToManyField(to='convivencia.SancionesGraves', verbose_name=b'Sanciones Graves', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanciones',
            name='SancionesLeves',
            field=models.ManyToManyField(to='convivencia.SancionesLeves', verbose_name=b'Sanciones Leves', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanciones',
            name='SancionesOtras',
            field=models.ManyToManyField(to='convivencia.SancionesOtras', verbose_name=b'Otras Sanciones', blank=True),
            preserve_default=True,
        ),
    ]
