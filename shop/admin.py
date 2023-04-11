from django.contrib import admin
from .models import Product, Brand, Category, Line


admin.site.register(Category)
admin.site.register(Line)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'image']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'popular', 'image']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'popular']

    prepopulated_fields = {'slug': ('name',)}

