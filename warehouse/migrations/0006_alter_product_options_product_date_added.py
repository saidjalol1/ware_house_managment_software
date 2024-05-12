# Generated by Django 4.2.13 on 2024-05-11 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_product_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 5, 11, 8, 49, 36, 431466, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
