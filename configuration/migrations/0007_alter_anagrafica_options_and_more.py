# Generated by Django 4.2.5 on 2023-10-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0006_alter_lesson_descrizione_alter_lesson_nome_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anagrafica',
            options={'verbose_name': 'Anagrafica', 'verbose_name_plural': 'Anagrafiche'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tipologia_lezione',
            field=models.CharField(choices=[('Gruppo', 'Gruppo'), ('Privata', 'Privata')], max_length=10, verbose_name='Tipologia Lezione:'),
        ),
    ]
