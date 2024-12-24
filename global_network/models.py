from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class GlobalBanner(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    def __str__(self):
        return self.title

class GlobalNetwork(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')  # Replace CKEditor5Field

    def __str__(self):
        return self.title

class GlobalNetworkData(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    def __str__(self):
        return self.title
