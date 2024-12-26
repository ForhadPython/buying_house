from django.contrib import admin
from django.utils.html import format_html
from .models import SustainabilityBanner, SustainabilityAbout, OurPartner, OurPartnerSlider


@admin.register(SustainabilityBanner)
class SustainabilityBannerAdmin(admin.ModelAdmin):
    list_display = ('banner_title', 'image_preview')
    search_fields = ('banner_title',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.banner_image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.banner_image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(SustainabilityAbout)
class SustainabilityAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

    def __str__(self):
        return self.title


@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner_desc')
    search_fields = ('partner_desc',)
    list_filter = ('id',)


@admin.register(OurPartnerSlider)
class OurPartnerSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image_preview')
    search_fields = ('title', 'link')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"
