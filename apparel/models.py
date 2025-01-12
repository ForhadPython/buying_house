from django.db import models
from ckeditor.fields import RichTextField  # or RichTextUploadingField


class ApparelsBanner(models.Model):
    image = models.ImageField(upload_to='carousel', null=True, blank=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')

    class Meta:
        verbose_name = "Apparels Banner"
        verbose_name_plural = "Apparels Banners"

    def __str__(self):
        return self.title


class ApparelsCategory(models.Model):
    category = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Apparels Category"
        verbose_name_plural = "Apparels Categories"

    def __str__(self):
        return self.category


class ApparelsGender(models.Model):
    gender = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Apparels Gender"
        verbose_name_plural = "Apparels Genders"

    def __str__(self):
        return self.gender


class ApparelsProduct(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=150)
    description = RichTextField(config_name='default')
    category = models.ForeignKey(ApparelsCategory, on_delete=models.CASCADE, related_name='products')
    gender = models.ForeignKey(ApparelsGender, on_delete=models.CASCADE, related_name='products')
    link = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Apparels Product"
        verbose_name_plural = "Apparels Products"

    def __str__(self):
        return self.title
