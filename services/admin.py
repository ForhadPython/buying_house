from django.contrib import admin
from .models import ServiceBanner, ServiceData, WorkTogether


@admin.register(ServiceBanner)
class ServiceBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)


@admin.register(ServiceData)
class ServiceDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_desc', 'link')
    search_fields = ('title', 'short_desc')
    list_filter = ('title',)


@admin.register(WorkTogether)
class WorkTogetherAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
