from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProfile(User):
    telegram = models.CharField(max_length=100)

    def __str__(self):
        return self.username