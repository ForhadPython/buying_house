from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now


# Home Section
class HomeBanner(models.Model):
    video_url = models.URLField(blank=True, null=True)
    start_at = models.IntegerField(default=1, null=True, blank=True)
    mute = models.BooleanField(default=False, null=True, blank=True)
    auto_play = models.BooleanField(default=True, null=True, blank=True)
    loop = models.BooleanField(default=True, null=True, blank=True)
    opacity = models.IntegerField(default=0)
    show_controls = models.BooleanField(default=True, null=True, blank=True)
    show_yt_logo = models.BooleanField(default=False, null=True, blank=True)
    volume = models.IntegerField(default=25, null=True, blank=True)
    short_title = models.CharField(max_length=990, null=True, blank=True)
    title = models.CharField(max_length=60, default="Untitled", null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    is_video = models.BooleanField(default=False)


class HomeBannerImage(models.Model):
    home_banner = models.ForeignKey(HomeBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_banner_images/')
    caption = models.CharField(max_length=255, null=True, blank=True)


class HomeAbout(models.Model):
    image = models.ImageField(upload_to='about_images/', null=True,blank=True)
    title = models.CharField(max_length=150,null=True, blank=True)
    short_desc = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    link = models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return self.title


class OurServiceData(models.Model):
    image = models.ImageField(upload_to='service-data/', null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Product Section
class OurProduct(models.Model):
    image = models.ImageField(upload_to='products-info/',null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = RichTextField(null=True, blank=True)
    link = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name


# Competitive Advantage Section

class CompetitiveAdvantageImg(models.Model):
    image = models.ImageField(upload_to='competitive/',null=True,blank=True)


class CompetitiveAdvantageInfo(models.Model):
    icon = models.ImageField(upload_to='competitive-icon/', null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class OurFeatureImg(models.Model):
    image = models.ImageField(upload_to='featureImg/', null=True, blank=True)


class OurFeatureInfo(models.Model):
    icon = models.ImageField(upload_to='feature-icon/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class FeatureSlider(models.Model):
    """Model for the Testimonials section"""
    description = RichTextField(null=True, blank=True)
    short_title = models.CharField(max_length=200,null=True, blank=True)
    short_name = models.CharField(max_length=100,null=True, blank=True)
    background_image = models.ImageField(upload_to='feature-slider/', null=True, blank=True)

    def __str__(self):
        return self.short_name

class FeatureSliderImage(models.Model):
    """Model for the Testimonials section"""
    background_image = models.ImageField(upload_to='feature-slider/', null=True, blank=True)


class HowWeWork(models.Model):
    image = models.ImageField(upload_to='how-we-work/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    image = models.ImageField(upload_to='why-choose-us/', null=True, blank=True)
    title = models.CharField(max_length=100,null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Model for Team Member
class MeetOurTeam(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    role = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='team_images/',null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


# Model for Blog Post
class BlogPost(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = RichTextField(config_name='default',null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/',null=True, blank=True)
    comments_count = models.IntegerField(default=0,null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)  # Add this line

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