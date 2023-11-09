from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sanciones',
            name='Fecha_incorporacion',
        ),
    ]
