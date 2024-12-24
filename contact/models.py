from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class ContactBanner(models.Model):
    image = models.ImageField(upload_to='Carousel', null=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = RichTextField(config_name='default')  # Replace CKEditor5Field

    def __str__(self):
        return self.full_name


class AdditionalInfo(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='default')  # Replace CKEditor5Field

    def __str__(self):
        return self.title


class BusinessHours(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='default')  # Replace CKEditor5Field

    def __str__(self):
        return self.title
