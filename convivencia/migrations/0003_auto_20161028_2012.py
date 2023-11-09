from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0002_remove_sanciones_fecha_incorporacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanciones',
            name='Sancion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
