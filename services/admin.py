from django.contrib import admin
from .models import ServiceBanner, ServiceData,WorkTogether


@admin.register(ServiceBanner)
class ServiceBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title field
    list_filter = ('title',)  # Adds a filter for the title field


@admin.register(ServiceData)
class ServiceDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'link')  # Displays key fields in the list view
    search_fields = ('title', 'short_desc')  # Adds search functionality for title and short description
    list_filter = ('title',)  # Adds a filter for the title field


@admin.register(WorkTogether)
class WorkTogetherAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_preview', 'link')
    search_fields = ('title', 'description', 'link')
    list_filter = ('title',)

    def description_preview(self, obj):
        # Display a short preview of the description
        return obj.description[:75] + '...' if len(obj.description) > 75 else obj.description

    description_preview.short_description = 'Description Preview'
