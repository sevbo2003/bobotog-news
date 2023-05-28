from django.contrib import admin
from apps.blog.models import Category, Post, PostImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    list_display_links = ('name', 'image')
    search_fields = ('name',)
    list_per_page = 10


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_featured','dolzarb', 'views')
    readonly_fields = ('views', 'created_at', 'updated_at')
    search_fields = ('title', 'category__name')
    list_filter = ('is_featured', 'dolzarb')
    list_per_page = 10
    inlines = [PostImageInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)