from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0006_auto_20161106_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]
