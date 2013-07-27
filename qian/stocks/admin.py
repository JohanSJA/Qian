from django.contrib import admin

from models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["code", "description", "type"]

admin.site.register(Category, CategoryAdmin)
