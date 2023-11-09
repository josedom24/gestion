from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='Idc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.ClaseDocumento'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Idp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Procedencia'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='Idr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Remitente'),
        ),
    ]
