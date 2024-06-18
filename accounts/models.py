from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=100, blank=False)
    address = models.TextField(blank=False)

    def __str__(self):
        return self.username
