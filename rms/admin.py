from django.contrib import admin
from .models import Category, Food, Table, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    search_fields = ['name']
    list_filter = ['category']
    list_per_page = 10
# class TableAdmin(admin.ModelAdmin):
#     list_display=['id','name','capacity','is_available']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'table', 'status', 'price', 'payment']
    list_filter = ['status', 'table', 'payment']
    
    

