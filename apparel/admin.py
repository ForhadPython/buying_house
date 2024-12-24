from django.contrib import admin
from .models import ApparelsBanner, ApparelsCategory, ApparelsGender, ApparelsType, ApparelsProduct


@admin.register(ApparelsBanner)
class ApparelsBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Displays title and image in the list view
    search_fields = ('title',)  # Enables a search box for the title


@admin.register(ApparelsCategory)
class ApparelsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)  # Displays category in the list view
    search_fields = ('category',)  # Enables a search box for the category


@admin.register(ApparelsGender)
class ApparelsGenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)  # Displays gender in the list view
    search_fields = ('gender',)  # Enables a search box for the gender


@admin.register(ApparelsType)
class ApparelsTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)  # Displays type in the list view
    search_fields = ('type',)  # Enables a search box for the type


@admin.register(ApparelsProduct)
class ApparelsProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'gender', 'type', 'image', 'link')  # Displays product details in the list view
    search_fields = ('title', 'category__category', 'gender__gender', 'type__type')  # Enables search for related fields
    list_filter = ('category', 'gender', 'type')  # Adds filters for category, gender, and type
    autocomplete_fields = ('category', 'gender', 'type')  # Enables autocomplete for ForeignKey fields
