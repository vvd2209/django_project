from django.contrib import admin

from blog.models import Blog
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'product')
    list_filter = ('is_active',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'data_create', 'is_publish', 'slug',)
    list_filter = ('data_create',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
