# Generated by Django 3.0.3 on 2020-02-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_remove_config_hi'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='include_numbers',
            field=models.BooleanField(default=False),
        ),
    ]
