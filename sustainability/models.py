from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class SustainabilityBanner(models.Model):
    banner_image = models.ImageField(upload_to='static/media/sustain-banner', null=True, blank=True)
    banner_title = models.CharField(max_length=150, null=True, blank=True)
    banner_description = RichTextField(config_name='default', null=True, blank=True)

    def __str__(self):
        return self.banner_title


class SustainabilityAbout(models.Model):
    image = models.ImageField(upload_to='static/media/sustain-about', null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextField(config_name='default', null=True, blank=True)

    def __str__(self):
        return self.title


class OurPartner(models.Model):
    partner_desc = RichTextField(config_name='default', null=True, blank=True)  # Replace CKEditor5Field


class OurPartnerSlider(models.Model):
    image = models.ImageField(upload_to='static/media/partner-slider', null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
