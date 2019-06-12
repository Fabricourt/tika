# Generated by Django 2.2.2 on 2019-06-10 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0003_lessor_onhire_truck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('booking_date', models.DateTimeField(blank=True, null=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
                ('unapproved', models.BooleanField(blank=True, default=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('Person_hiring_the_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
