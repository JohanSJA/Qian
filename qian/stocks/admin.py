from django.contrib import admin

from models import Category, Stock

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["code", "description", "type"]

class StockAdmin(admin.ModelAdmin):
    list_display = ["code", "category", "discontinued"]
    list_filter = ["category", "discontinued"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
