# Generated by Django 4.2.17 on 2025-01-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='auto_play',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='loop',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='mute',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='short_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='show_controls',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='show_yt_logo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='start_at',
            field=models.IntegerField(blank=True, default=18, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homebanner',
            name='volume',
            field=models.IntegerField(blank=True, default=25, null=True),
        ),
    ]
