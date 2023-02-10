from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extensible user model for possible future use
    """

    def __str__(self):
        return self.username
