# Generated by Django 4.2.17 on 2024-12-19 21:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Image')),
                ('title', models.CharField(max_length=150)),
                ('short_desc', ckeditor.fields.RichTextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('link', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AboutBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Image')),
                ('title', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Carousel')),
                ('title', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField()),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SliderTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]