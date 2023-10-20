# Generated by Django 4.2.5 on 2023-10-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0005_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='descrizione',
            field=models.TextField(blank=True, help_text='Inserisci una rapida descrizione dell attività svolta durante il corso. Non usare testi troppo lunghi, consigliamo massimo 50 parole', null=True, verbose_name='Descrizione'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='nome',
            field=models.CharField(help_text='Inserisci il nome del corso (Pilates, Yoga, ecc..)', max_length=23, verbose_name='Nome corso ( max 23 caratteri )'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tipologia_lezione',
            field=models.CharField(choices=[('1', 'Gruppo'), ('2', 'Private')], max_length=1, verbose_name='Tipologia Lezione:'),
        ),
    ]