from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class AccessoriesBanner(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    def __str__(self):
        return self.title

class AccessoriesData(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    short_desc = RichTextField(config_name='default')
    description = RichTextField(config_name='default')
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title