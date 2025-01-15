from django.db import models
from ckeditor.fields import RichTextField


class ServiceBanner(models.Model):
    image = models.ImageField(upload_to='Carousel', blank=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    def __str__(self):
        return self.title


class ServiceData(models.Model):
    image = models.ImageField(upload_to='Carousel', blank=True)
    title = models.CharField(max_length=150)
    short_desc = RichTextField(config_name='default')
    description = RichTextField(config_name='default')
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class WorkTogether(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
