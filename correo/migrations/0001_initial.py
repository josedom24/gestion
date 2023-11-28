# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centro', '0004_auto_20161102_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Asunto', models.CharField(max_length=100)),
                ('Contenido', models.TextField(blank=True)),
                ('Destinatarios', models.ManyToManyField(to='centro.Profesores', verbose_name='Destinatarios')),
            ],
            options={
                'verbose_name': 'Correos',
                'verbose_name_plural': 'Correos',
            },
        ),
    ]