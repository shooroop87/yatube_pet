# Generated by Django 4.2.5 on 2023-10-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_anagrafica_telefono_cellulare_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anagrafica',
            name='partita_iva',
            field=models.TextField(blank=True, null=True, verbose_name='Partita Iva:'),
        ),
    ]
