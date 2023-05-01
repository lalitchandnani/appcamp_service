from django.db import models

class DietPlannerSetting(models.Model):
    openai_model_name = models.CharField(max_length=255)
    openai_api_key = models.CharField(max_length=255)
    prompt = models.CharField(max_length=4096)

    class Meta:
        app_label = 'diet_api'