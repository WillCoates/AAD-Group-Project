# Generated by Django 3.0.2 on 2020-02-05 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200204_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='enabled',
        ),
    ]
