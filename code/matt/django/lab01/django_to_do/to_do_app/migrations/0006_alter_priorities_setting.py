# Generated by Django 4.0.4 on 2022-05-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0005_alter_priorities_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priorities',
            name='setting',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=6),
        ),
    ]
