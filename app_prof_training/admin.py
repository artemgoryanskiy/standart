from django.contrib import admin
from .models import CategoryProfTrain, ProgramProfTrain


class AdminCategory(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'image',)
    prepopulated_fields = {'slug': ('title',)}


class AdminProgram(admin.ModelAdmin):
    list_display = ('title', 'code_num', 'class_num', 'slug', 'category')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CategoryProfTrain, AdminCategory)
admin.site.register(ProgramProfTrain, AdminProgram)


