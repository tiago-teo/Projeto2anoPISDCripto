'''
Importação do módulo models do Django:
Este módulo contém classes e funções para definir modelos, que são representações de tabelas no banco de dados.
'''
from django.db import models
from django.contrib.auth.models import User

#Módulos importado do 'models' do Django 
#Para armazenar os inputs do formulário, e os campos de texto que define tamanho máximo e que o campo pode estar vazio
class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nome_emp = models.CharField(max_length=200, blank=True, null=True)
    nome_colab = models.CharField(max_length=500, blank=True, null=True)
    emails = models.CharField(max_length=200, blank=True, null=True)
    passwd = models.CharField(max_length=200, blank=True, null=True)
    domain = models.CharField(max_length=200, blank=True, null=True)
    ipadd = models.CharField(max_length=200, blank=True, null=True)
    urls = models.CharField(max_length=200, blank=True, null=True)
    shodan_search = models.CharField(max_length=200, blank=True, null=True)
    google_dork = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_emp


#Para armazenar as informações dos resultados das pesquisas
class Result(models.Model):
    search = models.OneToOneField(Search, on_delete=models.CASCADE, default=1)
    email_leak = models.TextField(max_length=200, blank=True, null=True)
    domain_leak = models.TextField(max_length=200, blank=True, null=True)
    spf = models.TextField(max_length=200, blank=True, null=True)
    emp = models.TextField(max_length=200, blank=True, null=True)
    shodan = models.TextField(max_length=200, blank=True, null=True)
    dork = models.TextField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.email_leak