# Generated by Django 3.1 on 2023-12-28 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dejavu_app', '0003_auto_20231228_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noveldetail',
            name='novel_master_id',
        ),
    ]
