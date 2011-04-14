from django.contrib import admin
from django.db import models
from django import forms
from django.forms.models import inlineformset_factory

from models import *

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'parent',]
    list_filter = ('parent',)
    class Meta:
        model = ProductCategory


class ManufacturerAdmin(admin.ModelAdmin):
    class Meta:
        model = Manufacturer


class BrandAdmin(admin.ModelAdmin):
    class Meta:
        model = Brand

class StockItemInline(admin.StackedInline):
    model = StockItem
    extra = 0
    filter_horizontal = ('attributes',)

class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductImage

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    filter_horizontal = ('attributes',)

class ProductRelationshipInline(admin.TabularInline):
    model = ProductRelationship
    fk_name = 'from_product'
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        StockItemInline,
        ProductImageInline,
        ProductRelationshipInline,
    ]
    list_display = ('title', 'category', 'brand',)
    list_filter = ('category', 'brand',)
    search_fields = ['sku', 'title', 'stock__package_title']
    
    class Meta:
        model = Product

class StockItemAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value',)
    class Meta:
        model = StockItemAttributeValue

class StockItemAttributeValueInline(admin.TabularInline):
    model = StockItemAttributeValue

class StockItemAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        StockItemAttributeValueInline,
    ]
    class Meta:
        model = StockItemAttribute

class StockItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'inventory')
    filter_horizontal = ('attributes',)

    class Meta:
        model = StockItem


class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'price')
    class Meta:
        model = PriceHistory

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('stock_item', 'quantity', 'cart')
    class Meta:
        model = CartItem


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(PriceHistory, PriceHistoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(StockItem, StockItemAdmin)
admin.site.register(StockItemAttribute, StockItemAttributeAdmin)
admin.site.register(StockItemAttributeValue, StockItemAttributeValueAdmin)
