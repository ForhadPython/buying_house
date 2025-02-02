# Generated by Django 4.2.17 on 2025-01-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handi_craft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handicraftbanner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carousel/banners/'),
        ),
        migrations.AlterField(
            model_name='handicraftdata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carousel/handicrafts/'),
        ),
        migrations.AlterField(
            model_name='handicraftdata',
            name='link',
            field=models.URLField(max_length=500),
        ),
    ]
