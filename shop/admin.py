from django.contrib import admin
from .models import Product, Brand, Category


admin.site.register(Brand)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'popular', 'image']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'popular']

    prepopulated_fields = {'slug': ('name',)}
