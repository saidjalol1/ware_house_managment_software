# Generated by Django 4.2.13 on 2024-05-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_alter_sale_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
