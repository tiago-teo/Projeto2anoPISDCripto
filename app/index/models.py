from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Classe para armazenar informações relacionadas com o hasking de passwords
class Hashing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    #Campo para armazenar o salt usado no hashing da password
    salt = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username