# CharField: Campo de texto simples.
nome = forms.CharField(max_length=100)

# IntegerField: Campo para números inteiros.
idade = forms.IntegerField()

# FloatField: Campo para números de ponto flutuante.
preco = forms.FloatField()

# DecimalField: Campo para números decimais.
valor = forms.DecimalField(max_digits=5, decimal_places=2)

# BooleanField: Campo para valores booleanos (True/False).
ativo = forms.BooleanField()

# DateField: Campo para datas.
data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# TimeField: Campo para horas.
hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

# DateTimeField: Campo para data e hora.
evento = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

# EmailField: Campo para endereços de email.
email = forms.EmailField()

# URLField: Campo para URLs.
site = forms.URLField()

# SlugField: Campo para "slugs" (sequências curtas e únicas, geralmente usadas em URLs).
slug = forms.SlugField()

# ChoiceField: Campo para uma escolha entre várias opções.
cor = forms.ChoiceField(choices=[('R', 'Red'), ('G', 'Green'), ('B', 'Blue')])

# MultipleChoiceField: Campo para selecionar múltiplas opções.
cores = forms.MultipleChoiceField(choices=[('R', 'Red'), ('G', 'Green'), ('B', 'Blue')])

# FileField: Campo para upload de arquivos.
arquivo = forms.FileField()

# ImageField: Campo para upload de imagens.
imagem = forms.ImageField()

# PasswordField: Campo para entrada de senhas (oculta os caracteres digitados).
senha = forms.CharField(widget=forms.PasswordInput())

# RegexField: Campo que valida a entrada com uma expressão regular.
codigo = forms.RegexField(regex=r'^[0-9]{4}$')

# IPAddressField: Campo para endereços IPv4 ou IPv6.
ip_address = forms.GenericIPAddressField(protocol='both')

#UUIDField: Campo para identificadores UUID.
uuid = forms.UUIDField()