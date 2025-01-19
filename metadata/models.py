from django.db import models
from ckeditor.fields import RichTextField


class UnifiedModel(models.Model):
    # Fields from AboutCompany
    about_company_image = models.ImageField(upload_to='about_company_posts/', blank=True, null=True)
    about_company_date = models.DateField(blank=True, null=True)
    about_company_description = RichTextField(blank=True, null=True)

    # Fields from ContactInfo
    contact_info_address = models.TextField(blank=True, null=True)
    contact_info_phone = models.CharField(max_length=50, blank=True, null=True)
    contact_info_email = models.EmailField(blank=True, null=True)

    # Fields from FooterMaps
    footer_maps_image = models.ImageField(upload_to='footer_img/', blank=True, null=True)
    footer_maps_url = models.URLField(blank=True, null=True)
    footer_maps_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.contact_info_email:
            return self.contact_info_email
        elif self.important_link_title:
            return self.important_link_title
        else:
            return "UnifiedModel Entry"
