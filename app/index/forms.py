from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .encrypt import hash_pass, create_salt
from .models import Hashing

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        salt = create_salt()        
        user.set_password(hash_pass(self.cleaned_data["password1"], salt))  # Altera a senha antes de salvar
        if commit:
            user.save()
            Hashing.objects.create(user=user, salt=salt)
        return user