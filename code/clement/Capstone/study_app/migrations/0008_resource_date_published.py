# Generated by Django 4.0.5 on 2022-06-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_app', '0007_rename_projects_resource_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='date_published',
            field=models.DateField(default=True),
            preserve_default=False,
        ),
    ]
