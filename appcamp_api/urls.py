from django.urls import path
from .views import notify_request

urlpatterns = [
    path('notify_request/', notify_request, name='notify_request'),
]
