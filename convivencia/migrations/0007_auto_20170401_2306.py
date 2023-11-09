from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0006_auto_20170401_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiposamonestaciones',
            options={'verbose_name': 'Tipo Amonestaci\xf3n', 'verbose_name_plural': 'Tipos de Amonestaciones'},
        ),
        migrations.AddField(
            model_name='amonestaciones',
            name='Tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Tipo_de', to='convivencia.TiposAmonestaciones'),
        ),
    ]
