from django.contrib import admin
from .models import Product, Category, ProductReview
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'stock_level',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(ProductReview)

