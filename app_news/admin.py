from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'image', 'body', 'publish', 'created', 'updated', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'


admin.site.register(Post, PostAdmin)







