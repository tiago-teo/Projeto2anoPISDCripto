from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hashing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    salt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username