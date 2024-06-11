# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver

# from .models import Hashing


# @receiver(post_save, sender=User)
# def create_hashing(sender, instance, created, **kwargs):
#     if created:
#         Hashing.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_hashing(sender, instance, **kwargs):
#     instance.hashing.save()