# Generated by Django 3.1 on 2023-12-30 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dejavu_app', '0003_auto_20231222_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='novel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dejavu_app.noveldetail', verbose_name='対象小説'),
        ),
    ]
