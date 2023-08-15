from django.contrib import admin
from .models import Product


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'image')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, AdminProduct)