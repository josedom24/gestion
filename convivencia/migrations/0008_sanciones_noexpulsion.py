from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0007_auto_20170401_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanciones',
            name='NoExpulsion',
            field=models.BooleanField(default=False),
        ),
    ]
