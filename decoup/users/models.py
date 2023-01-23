from django.contrib.auth.models import AbstractUser  # noqa
from django.db import models


class User(AbstractUser):
    """Custom User model"""

    name = models.CharField(blank=True, max_length=100)

    def __str__(self) -> str:
        return self.email
