# Generated by Django 5.1 on 2024-08-13 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_skill_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='skills',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'about', 'verbose_name_plural': 'abouts'},
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]