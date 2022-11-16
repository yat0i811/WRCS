# Generated by Django 4.1.2 on 2022-11-11 01:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wrcsystem', '0005_mapdanger'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterHigh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RaspberryPi_Name', models.CharField(max_length=16)),
                ('high', models.DecimalField(decimal_places=3, max_digits=4)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
