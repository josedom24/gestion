from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0004_tiposamonestaciones'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiposamonestaciones',
            options={'verbose_name': 'Tipo Ampnestaci\xf3n', 'verbose_name_plural': 'Tipo Amonestaciones'},
        ),
    ]
