from django.contrib import admin
from .models import Category, SubCategory, Product


@admin.register(Category)
class ModelCategory(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(SubCategory)
class ModelSubCategory(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'created_at']


@admin.register(Product)
class ModelProduct(admin.ModelAdmin):
    list_display = ['name', 'sub_id', 'created_at']
