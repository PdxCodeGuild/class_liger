# Generated by Django 4.0.5 on 2022-06-17 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=300)),
                ('due_date', models.DateField(null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('url', models.CharField(max_length=300)),
                ('resources_type', models.CharField(max_length=50)),
                ('date_published', models.DateField(null=True)),
                ('projects', models.ManyToManyField(related_name='resource', to='study_app.project')),
            ],
        ),
    ]
