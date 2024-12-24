from django.contrib import admin
from .models import (
    SustainabilityBanner,
    SustainabilityAbout,
    OurPartner,
    OurPartnerSlider
)


@admin.register(SustainabilityBanner)
class SustainabilityBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(SustainabilityAbout)
class SustainabilityAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'description')
    search_fields = ('title', 'short_desc', 'description')
    list_filter = ('title',)

@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(OurPartnerSlider)
class OurPartnerSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link')
    search_fields = ('title', 'link')
    list_filter = ('title',)
