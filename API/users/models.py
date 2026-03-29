from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    email = models.CharField(unique=False, blank=True, null=True)

    last_name = None
    first_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []