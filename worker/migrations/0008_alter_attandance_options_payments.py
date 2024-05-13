# Generated by Django 4.2.13 on 2024-05-13 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0007_alter_attandance_come_alter_attandance_leave'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attandance',
            options={'ordering': ['-date_added']},
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('type', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='worker.worker')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]