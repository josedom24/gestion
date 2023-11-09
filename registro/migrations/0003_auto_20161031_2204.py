from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20161030_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='Idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.ClaseDocumento'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Idp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Procedencia'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Idr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Remitente'),
        ),
    ]
