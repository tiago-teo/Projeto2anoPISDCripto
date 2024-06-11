from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from index.encrypt import decrypt

def upload_place_pics(instance, filename):
    return "fotos/{user}/{filename}".format(user=instance.user, filename=filename)

def upload_place_files(instance, filename):
    return "curriculos/{user}/{filename}".format(user=instance.user, filename=filename)

def default_place_pics():
    return "fotos/nopic.png"

def default_place_files():
    return "curriculos/default.txt"


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=100, default="")
    foto = models.ImageField(upload_to=upload_place_pics, null=True, blank=True)
    intelx_api = models.CharField(max_length=5000, default="")
    hunter_api = models.CharField(max_length=5000, default="")
    shodan_api = models.CharField(max_length=5000, default="")
    
    @property
    def get_photo_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return "/static/nopic.png"

    def get_intelx_api(self):
        return decrypt(self.intelx_api.encode())

    def get_hunter_api(self):
        return decrypt(self.hunter_api.encode())

    def get_shodan_api(self):
        return decrypt(self.shodan_api.encode())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.foto and self.foto.path:
            try:
                img = Image.open(self.foto.path)

                if img.height > 200 or img.width > 200:
                    new_img = (200, 200)
                    img.thumbnail(new_img)
                    img.save(self.foto.path)
            except Exception as e:
                # Handle the case where the image file is not accessible or any other error
                print(f"Error processing image: {e}")

    def __str__(self):
        return self.nome
