# Generated by Django 3.2.23 on 2023-12-24 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dejavu_app', '0005_novels_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novels',
            name='number',
        ),
    ]
