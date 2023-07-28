from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "publication_flag", "created_at")
