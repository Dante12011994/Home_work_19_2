from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Version)
class Vesionadmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'number_vers',)
    list_filter = ('product',)
