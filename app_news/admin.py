from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'image', 'body', 'publish', 'created', 'updated', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)







