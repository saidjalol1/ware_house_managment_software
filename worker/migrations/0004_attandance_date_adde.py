# Generated by Django 4.2.13 on 2024-05-12 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_attandance_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='attandance',
            name='date_adde',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
