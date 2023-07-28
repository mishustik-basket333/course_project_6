from django.contrib import admin

from clients.models import Client, Mail, Mailings, Log


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name",)
    list_filter = ("owner",)
    search_fields = ("name", "email",)


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ("id", "time", "date", "time")


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "owner",)
    list_filter = ("owner",)
    search_fields = ("subject",)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("id", "status",)
    list_filter = ("mailing",)
    search_fields = ("mailing",)
