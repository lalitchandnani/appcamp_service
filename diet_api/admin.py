from django.contrib import admin
from .models import DietPlannerSetting

@admin.register(DietPlannerSetting)
class DietPlannerSettingsAdmin(admin.ModelAdmin):
    list_display = ('openai_model_name',)
