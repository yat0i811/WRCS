# Generated by Django 4.1.2 on 2023-01-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrcsystem', '0011_rename_inputwater_flg_wrcsall_inwater_flg'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrcsall',
            name='ras_name',
            field=models.CharField(default='NoName', max_length=16, null=True),
        ),
    ]