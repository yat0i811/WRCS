# Generated by Django 4.1.2 on 2022-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrcsystem', '0003_watertemperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watertemperature',
            name='celsius',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertemperature',
            name='fahrenheit',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]