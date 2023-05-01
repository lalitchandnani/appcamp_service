from django.contrib import admin
from .models import AppCampSetting

@admin.register(AppCampSetting)
class AppCampSettingsAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'recipient_email')
