from django.contrib import admin
from .models import ApparelsBanner, ApparelsCategory, ApparelsGender, ApparelsProduct
from django.utils.html import format_html

@admin.register(ApparelsBanner)
class ApparelsBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')  # Displays title and image preview
    search_fields = ('title',)  # Enables a search box for the title
    readonly_fields = ('image_preview',)  # Adds an image preview as readonly

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'


@admin.register(ApparelsCategory)
class ApparelsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)  # Displays category in the list view
    search_fields = ('category',)  # Enables a search box for the category
    ordering = ('category',)  # Orders by category alphabetically


@admin.register(ApparelsGender)
class ApparelsGenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)  # Displays gender in the list view
    search_fields = ('gender',)  # Enables a search box for the gender
    ordering = ('gender',)  # Orders by gender alphabetically


@admin.register(ApparelsProduct)
class ApparelsProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'gender', 'image_preview', 'link')  # Displays product details in the list view
    search_fields = ('title', 'category__category', 'gender__gender')  # Enables search for related fields
    list_filter = ('category', 'gender')  # Adds filters for category and gender
    autocomplete_fields = ('category', 'gender')  # Enables autocomplete for ForeignKey fields
    readonly_fields = ('image_preview',)  # Adds an image preview as readonly
    ordering = ('title',)  # Orders by product title alphabetically

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
