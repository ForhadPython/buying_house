from django.contrib import admin
from .models import HandiCraftBanner, HandiCraftData
from ckeditor.widgets import CKEditorWidget


class HandiCraftBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)


class HandiCraftDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', 'short_desc', 'description')
    list_filter = ('title',)
    ordering = ('title',)


admin.site.register(HandiCraftBanner, HandiCraftBannerAdmin)
admin.site.register(HandiCraftData, HandiCraftDataAdmin)
