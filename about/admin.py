from django.contrib import admin
from .models import AboutBanner, About, SliderTitle, AboutSlider


@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title
    list_filter = ('title',)  # Adds filtering by title


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'link')  # Displays key fields in the admin list view
    search_fields = ('title', 'short_desc')  # Adds search functionality for title and short description
    list_filter = ('title',)  # Adds filtering by title


@admin.register(SliderTitle)
class SliderTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Displays title in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title
    list_filter = ('title',)  # Adds filtering by title


@admin.register(AboutSlider)
class AboutSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link')  # Displays title, image, and link
    search_fields = ('title', 'description')  # Adds search functionality for title and description
    list_filter = ('title',)  # Adds filtering by title
