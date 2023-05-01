from django.contrib import admin
from .models import Product, Brand, Category, Line


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'image']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'image']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'image']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'popular', 'image']
    list_filter = ['available', 'created', 'updated', 'brnd', 'line', 'cat']
    list_editable = ['price', 'available', 'popular']

    prepopulated_fields = {'slug': ('name',)}

