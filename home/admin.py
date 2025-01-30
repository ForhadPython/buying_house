from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


# Custom form for RichTextField in admin
class AboutForm(forms.ModelForm):
    short_desc = forms.CharField(widget=CKEditorWidget(), required=False)
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = HomeAbout
        fields = '__all__'


# Inline admin for HomeBannerImage
class HomeBannerImageInline(admin.TabularInline):
    model = HomeBannerImage
    extra = 1  # Number of extra forms to display
    verbose_name = "Banner Image"
    verbose_name_plural = "Banner Images"


# Admin for HomeBanner
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'is_video', 'video_url']
    list_editable = ['is_video', 'video_url']
    inlines = [HomeBannerImageInline]


# Admin for HomeAbout with CKEditor
class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image')
    search_fields = ('title', 'link')
    form = AboutForm  # Use CKEditor for rich text fields


# Registering models with custom and default admin classes
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(OurServiceData)
admin.site.register(OurProduct)
admin.site.register(CompetitiveAdvantageImg)
admin.site.register(CompetitiveAdvantageInfo)
admin.site.register(OurFeatureImg)
admin.site.register(OurFeatureInfo)
# admin.site.register(FeatureSliderImage)
# admin.site.register(FeatureSlider)
admin.site.register(HowWeWork)
admin.site.register(WhyChooseUs)
# admin.site.register(MeetOurTeam)
admin.site.register(BlogPost)
# admin.site.register(GlobalCollaboration)
# admin.site.register(GlobalCollaborationOffice)