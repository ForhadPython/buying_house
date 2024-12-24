from django.db import models
from ckeditor.fields import RichTextField


class AboutCompany(models.Model):
    image = models.ImageField(upload_to='about_company_posts/')
    date = models.DateField()
    description = RichTextField()


class ImportantLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class FooterMaps(models.Model):
    image = models.ImageField(upload_to='widget_posts/')
    url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.date

