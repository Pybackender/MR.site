# Generated by Django 5.1 on 2024-08-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'skill', 'verbose_name_plural': 'skills'},
        ),
    ]