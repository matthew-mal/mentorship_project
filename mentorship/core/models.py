from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_mentor = models.BooleanField(default=False)
    mentor = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="mentees"
    )

    def __str__(self):
        return self.username
