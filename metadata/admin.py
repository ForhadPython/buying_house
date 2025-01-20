from django.contrib import admin
from .models import UnifiedModel


@admin.register(UnifiedModel)
class UnifiedModelAdmin(admin.ModelAdmin):
    list_display = (
        'contact_info_email',
        'contact_info_phone',
        'contact_info_address'
    )  # Fields to display in the list view
    search_fields = ('contact_info_email', 'contact_info_phone', 'contact_info_address')  # Searchable fields
    list_filter = ('contact_info_email',)  # Add a filter sidebar for email
    ordering = ('contact_info_email',)  # Default ordering
    fieldsets = (
        ('About Company', {
            'fields': ('about_company_image', 'about_company_description'),
        }),
        ('Contact Information', {
            'fields': ('contact_info_address', 'contact_info_phone', 'contact_info_email'),
        }),
        ('Footer Maps', {
            'fields': ('footer_maps_image', 'footer_maps_url'),
        }),
    )
