from django.db import models

class AppCampSetting(models.Model):
    sendgrid_api_key = models.CharField(max_length=255)
    sender_email = models.CharField(max_length=255)
    recipient_email = models.CharField(max_length=255)

    class Meta:
        app_label = 'appcamp_api'