from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

# Custom form for RichTextField in admin
class AboutForm(forms.ModelForm):
    class Meta:
        model = HomeAbout
        fields = '__all__'
    short_desc = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

# About Admin
class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image')
    search_fields = ('title', 'link')
    form = AboutForm  # To use the CKEditor for rich text fields

# Register your models here
admin.site.register(HomeBanner)
admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(OurServiceData)
admin.site.register(OurProduct)
admin.site.register(CompetitiveAdvantageImg)
admin.site.register(CompetitiveAdvantageInfo)
admin.site.register(OurFeatureImg)
admin.site.register(OurFeatureInfo)
admin.site.register(FeatureSlider)
admin.site.register(HowWeWork)
admin.site.register(WhyChooseUs)
admin.site.register(MeetOurTeam)
admin.site.register(BlogPost)
admin.site.register(GlobalCollaboration)
admin.site.register(GlobalCollaborationOffice)
admin.site.register(MetaData)
