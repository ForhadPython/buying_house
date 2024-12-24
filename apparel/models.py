from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class ApparelsBanner(models.Model):
    image = models.ImageField(upload_to='carousel', null=True, blank=True)  # Added blank=True for flexibility
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    def __str__(self):
        return self.title


class ApparelsCategory(models.Model):
    category = models.CharField(max_length=150, unique=True)  # Added unique=True to avoid duplicate categories

    def __str__(self):
        return self.category


class ApparelsGender(models.Model):
    gender = models.CharField(max_length=150, unique=True)  # Added unique=True to avoid duplicate gender entries

    def __str__(self):
        return self.gender


class ApparelsType(models.Model):
    type = models.CharField(max_length=150, unique=True)  # Added unique=True to avoid duplicate type entries

    def __str__(self):
        return self.type


class ApparelsProduct(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)  # Changed upload path and added blank=True
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')
    category = models.ForeignKey(ApparelsCategory, on_delete=models.CASCADE, related_name='products')  # Added related_name for reverse lookups
    gender = models.ForeignKey(ApparelsGender, on_delete=models.CASCADE, related_name='products')  # Added related_name for reverse lookups
    type = models.ForeignKey(ApparelsType, on_delete=models.CASCADE, related_name='products')  # Added related_name for reverse lookups
    link = models.URLField(max_length=500)  # Changed to URLField for validation

    def __str__(self):
        return self.title
