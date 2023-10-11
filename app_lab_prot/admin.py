from django.contrib import admin
from .models import ProductLabProt


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'image')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ProductLabProt, AdminProduct)
