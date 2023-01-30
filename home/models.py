from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPassword(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    application_type = models.CharField(max_length=30)
    website_name = models.CharField(max_length=30)
    website_url = models.CharField(max_length=100)
    application_name = models.CharField(max_length=20)
    game_name = models.CharField(max_length=20)
    game_developer = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.website_name
