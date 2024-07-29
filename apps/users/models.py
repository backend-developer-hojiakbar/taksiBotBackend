from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    passport_photo = models.ImageField(upload_to='passport_photo/')
    prava_photo = models.ImageField(upload_to='prava_photo/')
    balance = models.PositiveIntegerField(default=0, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"