from django.contrib import admin
from .models import GlobalBanner, GlobalNetwork, GlobalNetworkData

# Register your models here.

@admin.register(GlobalBanner)
class GlobalBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(GlobalNetwork)
class GlobalNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(GlobalNetworkData)
class GlobalNetworkDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)
