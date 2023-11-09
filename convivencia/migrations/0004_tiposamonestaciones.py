from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0003_auto_20161028_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposAmonestaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoAmonestacion', models.CharField(max_length=60)),
            ],
        ),
    ]
