from django.contrib import admin
from apps.magazine.models import Magazine


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'hajmi', 'downloads_count']
    list_filter = ['created_at']
    search_fields = ['name']
    readonly_fields = ['hajmi', 'downloads_count']
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'file')
        }),
        ('Qo\'shimcha ma\'lumotlar', {
            'fields': ('created_at', 'hajmi', 'downloads_count')
        })
    )
    