# Generated by Django 4.2.17 on 2025-01-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homebanner_auto_play_alter_homebanner_mute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='loop',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
