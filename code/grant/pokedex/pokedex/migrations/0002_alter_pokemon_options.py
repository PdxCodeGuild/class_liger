# Generated by Django 4.0.4 on 2022-05-15 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'verbose_name_plural': 'Pokemon'},
        ),
    ]
