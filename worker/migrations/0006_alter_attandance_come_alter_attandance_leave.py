# Generated by Django 4.2.13 on 2024-05-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_rename_date_adde_attandance_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attandance',
            name='come',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='attandance',
            name='leave',
            field=models.TimeField(blank=True),
        ),
    ]
