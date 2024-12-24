from django.contrib import admin
from .models import ProductBanner, ProductAbout

# Register your models here.

@admin.register(ProductBanner)
class ProductBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(ProductAbout)
class ProductAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'short_desc', 'description', 'link')
    search_fields = ('title', 'short_desc', 'description', 'link')
    list_filter = ('title',)
