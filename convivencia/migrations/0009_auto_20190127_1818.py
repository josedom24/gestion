from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0008_sanciones_noexpulsion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanciones',
            name='NoExpulsion',
            field=models.BooleanField(default=False, verbose_name='Medidas de flexibilizaci\xf3n a la expulsi\xf3n'),
        ),
    ]
