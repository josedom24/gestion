from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClaseDocumento', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Procedencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Procedencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Procedencia',
                'verbose_name_plural': 'Procedencias',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.CharField(max_length=9)),
                ('Fecha', models.DateField()),
                ('N', models.IntegerField()),
                ('Tipo', models.CharField(max_length=7)),
                ('Contenido', models.TextField(blank=True)),
                ('Idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.ClaseDocumento')),
                ('Idp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Procedencia')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Remitente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remitente', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Temitente',
                'verbose_name_plural': 'Remitentes',
            },
        ),
        migrations.AddField(
            model_name='registro',
            name='Idr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Remitente'),
        ),
    ]
