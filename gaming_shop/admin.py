from django.contrib import admin

# Register your models here.

from .models import Category, Product, Platform

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug', 'price', 
                    'developer', 'publisher', 'created',
                    'updated', 'in_stock', 'is_active']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name',]