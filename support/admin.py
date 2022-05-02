from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Message, Ticket, User


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'time_update', 'time_create', 'client')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'client')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'text', 'sender', 'time_create')
    list_display_links = ('ticket_id', 'text')
    list_filter = ('ticket', )


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(User, CustomUserAdmin)

admin.site.site_header = 'Админ-панель приложения Support'
