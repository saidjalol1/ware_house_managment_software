# Generated by Django 4.2.13 on 2024-05-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_remove_worker_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='attandance',
            name='paid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
