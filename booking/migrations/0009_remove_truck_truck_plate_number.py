# Generated by Django 2.2.2 on 2019-06-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20190611_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='truck_plate_number',
        ),
    ]
