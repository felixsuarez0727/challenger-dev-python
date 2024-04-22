# Generated by Django 5.0.4 on 2024-04-22 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.TextField(verbose_name='timestamp')),
                ('comments', models.TextField(verbose_name='comentarios')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infracciones', to='management.vehicle', verbose_name='license_plate')),
            ],
            options={
                'verbose_name': 'infracción',
                'verbose_name_plural': 'infracciones',
            },
        ),
    ]
