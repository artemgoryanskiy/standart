from django.contrib import admin
from .models import PostNews, CategoryNews, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'image', 'body', 'publish', 'created', 'updated', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PostNews, PostAdmin)
admin.site.register(CategoryNews, CategoryAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



