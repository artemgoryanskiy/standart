from django.contrib import admin
from .models import Category, Program


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'slug', 'image',)
    prepopulated_fields = {'slug': ('title',)}


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'hours', 'qualification', 'description', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Program, ProgramAdmin)