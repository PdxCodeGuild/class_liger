# Generated by Django 4.0.4 on 2022-05-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_priority_todoitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='low', max_length=6),
        ),
    ]
