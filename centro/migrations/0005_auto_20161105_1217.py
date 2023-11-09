from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0004_auto_20161102_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '\xc1rea',
                'verbose_name_plural': '\xc1reas',
            },
        ),
        migrations.AlterModelOptions(
            name='departamentos',
            options={},
        ),
        migrations.AddField(
            model_name='areas',
            name='Departamentos',
            field=models.ManyToManyField(blank=True, to='centro.Departamentos'),
        ),
    ]
