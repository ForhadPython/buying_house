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

class SliderTitle(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='default')  # Replace CKEditor5Field

    def __str__(self):
        return self.title

class AboutSlider(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title