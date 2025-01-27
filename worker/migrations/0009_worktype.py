# Generated by Django 4.2.13 on 2024-05-13 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_alter_product_options_product_date_added'),
        ('worker', '0008_alter_attandance_options_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('paid', models.PositiveBigIntegerField(default=0)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('work_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='warehouse.category')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='worker.worker')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
