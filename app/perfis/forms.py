from django import forms
from .models import Perfil
from index.encrypt import encrypt


class PerfilForm(forms.ModelForm):
    #Cria um Formulário com campos de texto para 'input' dos utilizadores para nome e para as APIs dos sites Intelx, Hunter e shodan. 
    #E cria um campo para dar upload a imagem de perfil do utilizador
    nome = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    intelx_api = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    hunter_api = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    shodan_api = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))

    class Meta:
        model = Perfil   #especifica que o formulário está associado ao modelo Perfil
        fields = ['nome', 'foto', 'intelx_api', 'hunter_api', 'shodan_api'] #Define os campos que são usados no formulário
    
    #Para campos que todos os campose sejam obrigatórios preencher
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
    
    #método para guardar os formulários dos utilizadores
    #e  #cria um perfil que guarda as APIs encriptadas na base de dados. As funções para encriptar encontram-se no ficheiro index/encrypt.py
    def save(self, commit=True):
        perfil = super(PerfilForm, self).save(commit=False)
        if self.cleaned_data['intelx_api']:
            perfil.intelx_api = encrypt(self.cleaned_data['intelx_api'])
        if self.cleaned_data['hunter_api']:
            perfil.hunter_api = encrypt(self.cleaned_data['hunter_api'])
        if self.cleaned_data['shodan_api']:
            perfil.shodan_api = encrypt(self.cleaned_data['shodan_api'])
        if commit:
            perfil.save()
        return perfil


