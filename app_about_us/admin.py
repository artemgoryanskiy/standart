from django.contrib import admin
from .models import Contact, Document


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'message',)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Document, DocumentAdmin)
