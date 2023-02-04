from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserPassword(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    application_type = models.CharField(max_length=30)
    website_name = models.CharField(max_length=30, blank=True)
    website_url = models.CharField(max_length=100, blank=True)
    application_name = models.CharField(max_length=20, blank=True)
    game_name = models.CharField(max_length=20, blank=True)
    game_developer = models.CharField(max_length=30, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
