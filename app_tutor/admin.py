from django.contrib import admin
from .models import Tutor, BecomeTutor

# Register your models here.


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'education', 'photo',
                    'description', 'subject', 'vk_link', 'phone', 'email', 'rate')


@admin.register(BecomeTutor)
class BecomeTutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'education', 'work_experience', 'phone', 'email')
