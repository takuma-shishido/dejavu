# Generated by Django 3.1 on 2024-01-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dejavu_app', '0004_auto_20240117_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='novel_id',
            field=models.IntegerField(),
        ),
    ]
