from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0005_auto_20161105_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentos',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
    ]
