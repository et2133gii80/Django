from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name',)
    search_fields = ('category_name','description',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)
