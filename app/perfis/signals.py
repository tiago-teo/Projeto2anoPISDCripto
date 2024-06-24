from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Perfil

# Metodos para que quando for detetado o registo de um novo utilizador (signal) seja criado um perfil correspondente a esse utilizador. As informações deste utilizador 
# podem ser atualizadas após o login

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.perfil.save()