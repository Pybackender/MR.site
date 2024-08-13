# Generated by Django 5.1 on 2024-08-13 07:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='The text must be unique', max_length=128, unique_for_month='published_at')),
                ('slug', models.CharField(max_length=128, unique_for_month='published_at')),
                ('status', models.IntegerField(choices=[(1, 'Send'), (2, 'Cancel')], default=2)),
                ('name', models.CharField(max_length=125)),
                ('positions', models.CharField(max_length=125)),
                ('content', models.CharField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'teams',
                'verbose_name_plural': 'team',
                'ordering': ['title'],
                'get_latest_by': ['-published_at'],
            },
        ),
    ]
