from django.contrib import admin
from .models import CategoryProfDev, ProgramProfDev


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'short_desc', 'audience_category', 'purpose', 'rate', 'slug', 'image')
    prepopulated_fields = {'slug': ('title',)}


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'hours', 'document', 'description', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CategoryProfDev, CategoryAdmin)
admin.site.register(ProgramProfDev, ProgramAdmin)