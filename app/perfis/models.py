from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from index.encrypt import decrypt

#Define uma função para encaminhar o upload das fotos dos utilizadores
def upload_place_pics(instance, filename):
    return "fotos/{user}/{filename}".format(user=instance.user, filename=filename)

#Caso o utilizador não dê upload a foto, fica com a foto default
def default_place_pics():
    return "fotos/nopic.png"


#Define um modelo Perfil que armazena as informações sobre o utilizador
#Define aind aos campos do perfil
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1) # Associa o id do utilizador ao id do perfil. Caso seja apagado o utilizador, o perfil é apagado também.
    nome = models.CharField(max_length=100, default="")
    foto = models.ImageField(upload_to=upload_place_pics, null=True, blank=True)
    intelx_api = models.CharField(max_length=5000, default="")
    hunter_api = models.CharField(max_length=5000, default="")
    shodan_api = models.CharField(max_length=5000, default="")
    
    @property
    def get_photo_url(self):
        #para ir buscar a foto uploaded, ou caso não tenha, vai buscar a default
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return "/static/nopic.png"

    #Guarda a imagem na base de dados e redimensiona a imagem do perfil para 
    #um tamanho de 200x200, para que a foto não fique desformatada no site
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
                #Caso a imagem não seja suportada
                print(f"Error processing image: {e}")

    def __str__(self):
        return self.nome
