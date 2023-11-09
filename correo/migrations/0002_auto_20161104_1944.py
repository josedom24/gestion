from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correos',
            name='Asunto',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='correos',
            name='Destinatarios',
            field=models.ManyToManyField(blank=True, to='centro.Profesores', verbose_name='Destinatarios'),
        ),
    ]
