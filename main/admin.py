# main/admin.py
from django.contrib import admin
from .models import ContactMessage
from .models import BugReport

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'date_submitted')

admin.site.register(BugReport)