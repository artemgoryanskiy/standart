from django.contrib import admin
from .models import CategoryProfDev, ProgramProfDev


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug', 'image',)
    prepopulated_fields = {'slug': ('title',)}


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'hours', 'description', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CategoryProfDev, CategoryAdmin)
admin.site.register(ProgramProfDev, ProgramAdmin)