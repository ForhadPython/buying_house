# Generated by Django 4.2.17 on 2024-12-21 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_ourfeature'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_logo', models.ImageField(upload_to='header-logo/')),
                ('about_company', models.ImageField(upload_to='header-logo/')),
                ('about_company_desc', models.TextField()),
                ('contact_info', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('maps_img', models.ImageField(upload_to='header-logo/')),
                ('maps_desc', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
