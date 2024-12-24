from django.contrib import admin
from .models import AccessoriesBanner, AccessoriesData


@admin.register(AccessoriesBanner)
class AccessoriesBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search for the title field
    list_filter = ('title',)  # Adds a filter for the title


@admin.register(AccessoriesData)
class AccessoriesDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'link')  # Displays key fields in the list view
    search_fields = ('title', 'short_desc')  # Adds search functionality for title and short description
    list_filter = ('title',)  # Adds a filter for the title field
