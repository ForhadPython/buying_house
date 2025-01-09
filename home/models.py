from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now


# Home Section
class HomeBanner(models.Model):
    video_url = models.URLField(blank=True, null=True)
    start_at = models.IntegerField(default=0, null=True, blank=True)
    mute = models.BooleanField(default=False, null=True, blank=True)
    auto_play = models.BooleanField(default=True, null=True, blank=True)
    loop = models.BooleanField(default=True, null=True, blank=True)
    opacity = models.IntegerField(default=1)
    show_controls = models.BooleanField(default=False, null=True, blank=True)
    show_yt_logo = models.BooleanField(default=False, null=True, blank=True)
    volume = models.IntegerField(default=25, null=True, blank=True)
    short_title = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=60, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    is_video = models.BooleanField(default=False)  # Checkbox to toggle between video and image slider

    def __str__(self):
        return self.title or 'Home Banner'


class HomeBannerImage(models.Model):
    home_banner = models.ForeignKey(HomeBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_banner_images/')
    caption = models.CharField(max_length=255, null=True, blank=True)  # Optional caption


class HomeAbout(models.Model):
    image = models.ImageField(upload_to='about_images/', null=True)
    title = models.CharField(max_length=150)
    short_desc = RichTextField()
    description = RichTextField()
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class OurServiceData(models.Model):
    image = models.ImageField(upload_to='service-data/', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# Product Section
class OurProduct(models.Model):
    image = models.ImageField(upload_to='products-info/', null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Competitive Advantage Section

class CompetitiveAdvantageImg(models.Model):
    image = models.ImageField(upload_to='competitive/', null=True)


class CompetitiveAdvantageInfo(models.Model):
    icon = models.ImageField(upload_to='competitive-icon/', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class OurFeatureImg(models.Model):
    image = models.ImageField(upload_to='featureImg/', null=True)


class OurFeatureInfo(models.Model):
    icon = models.ImageField(upload_to='feature-icon/', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class FeatureSlider(models.Model):
    """Model for the Testimonials section"""
    description = models.TextField()
    short_title = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='feature-slider/', null=True, blank=True)

    def __str__(self):
        return self.short_name


class HowWeWork(models.Model):
    image = models.ImageField(upload_to='how-we-work/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    image = models.ImageField(upload_to='why-choose-us/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# Model for Team Member
class MeetOurTeam(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_images/')
    description = models.TextField()

    def __str__(self):
        return self.name


# Model for Blog Post
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(config_name='default')
    image = models.ImageField(upload_to='blog_images/')
    comments_count = models.IntegerField(default=0)
    link = models.URLField()

    def __str__(self):
        return self.title


# Model for Global Collaboration Country
class GlobalCollaboration(models.Model):
    name = models.CharField(max_length=20)
    flag_image = models.ImageField(upload_to='country_flags/')

    def __str__(self):
        return self.name


# Model for Global Collaboration Country
class GlobalCollaborationOffice(models.Model):
    image = models.ImageField(upload_to='office-image/')
    link = models.URLField()

    def __str__(self):
        return self.link


class MetaData(models.Model):
    header_logo = models.ImageField(upload_to='header-logo/')
    about_company = models.ImageField(upload_to='header-logo/')
    about_company_desc = models.TextField()
    contact_info = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    maps_img = models.ImageField(upload_to='header-logo/')
    maps_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now, editable=False)  # Automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update every time the record is saved

    def __str__(self):
        return f"MetaData - {self.contact_info}"
