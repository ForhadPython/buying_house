from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class HandiCraftBanner(models.Model):
    image = models.ImageField(upload_to='carousel/banners/', null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextField(config_name='default', null=True, blank=True)

    def __str__(self):
        return self.title


class HandiCraftData(models.Model):
    image = models.ImageField(upload_to='carousel/handicrafts/', null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    short_desc = RichTextField(config_name='default', null=True, blank=True)
    description = RichTextField(config_name='default', null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)  # Use URLField instead of CharField for links

    def __str__(self):
        return self.title
