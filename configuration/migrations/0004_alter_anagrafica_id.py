# Generated by Django 4.2.5 on 2023-10-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_anagrafica_partita_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]