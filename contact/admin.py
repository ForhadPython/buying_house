from django.contrib import admin
from .models import Contact, AdditionalInfo, BusinessHours,ContactBanner

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

admin.site.register(ContactBanner)
