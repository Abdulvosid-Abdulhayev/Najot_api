# Generated by Django 5.1.3 on 2024-11-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
    ]