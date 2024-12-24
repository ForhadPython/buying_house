from django.contrib import admin
from .models import ProcessBanner, ProcessContent, ProcessData


@admin.register(ProcessBanner)
class ProcessBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title field
    list_filter = ('title',)  # Adds filtering by title


@admin.register(ProcessContent)
class ProcessContentAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Displays title in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title field
    list_filter = ('title',)  # Adds filtering by title


@admin.register(ProcessData)
class ProcessDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the admin list view
    search_fields = ('title',)  # Enables search functionality for the title field
    list_filter = ('title',)  # Adds filtering by title
