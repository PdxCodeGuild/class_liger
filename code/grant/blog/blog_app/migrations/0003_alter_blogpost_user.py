# Generated by Django 4.0.4 on 2022-05-13 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_blogpost_user_alter_blogpost_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
