# Generated by Django 5.1.1 on 2024-09-09 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('smtp_server', models.CharField(max_length=150)),
                ('smtp_port', models.IntegerField()),
                ('smtp_username', models.CharField(max_length=150)),
                ('smtp_password', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('url_logo', models.URLField()),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school_app_id', to='school.appsettingsmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
