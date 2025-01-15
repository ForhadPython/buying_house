from django.contrib import admin
from .models import AboutBanner, About


@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title
    list_filter = ('title',)  # Adds filtering by title


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'link')  # Displays key fields in the admin list view
    search_fields = ('title', 'short_desc')  # Adds search functionality for title and short description
    list_filter = ('title',)