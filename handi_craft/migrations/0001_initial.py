# Generated by Django 4.2.17 on 2025-01-29 08:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandiCraftBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Carousel')),
                ('title', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='HandiCraftData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Carousel')),
                ('title', models.CharField(max_length=150)),
                ('short_desc', ckeditor.fields.RichTextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
