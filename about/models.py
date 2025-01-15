from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class AboutBanner(models.Model):
    image = models.ImageField(upload_to='Image', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')


class About(models.Model):
    image = models.ImageField(upload_to='Image', null=True)
    title = models.CharField(max_length=150)
    short_desc = RichTextField(config_name='default')
    description = RichTextField(config_name='default')
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.title