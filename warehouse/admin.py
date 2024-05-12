from django.contrib import admin
from .models import Category, Product


admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
