# Generated by Django 4.1.2 on 2022-12-21 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrcsystem', '0007_alter_waterhigh_high_alter_watertemperature_celsius_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_image',
        ),
    ]
