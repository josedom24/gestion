from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20161031_2204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remitente',
            options={'verbose_name': 'Remitente', 'verbose_name_plural': 'Remitentes'},
        ),
    ]
