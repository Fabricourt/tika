# Generated by Django 2.2.2 on 2019-06-10 07:53

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('about_main_pic', models.ImageField(blank=True, null=True, upload_to='header/')),
                ('about_pic', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('our_numbers', models.CharField(blank=True, max_length=200, null=True)),
                ('reload', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
