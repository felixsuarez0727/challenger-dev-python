# Generated by Django 5.0.4 on 2024-04-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offenseAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offense',
            name='timestamp',
            field=models.TextField(verbose_name='timestamp'),
        ),
    ]
