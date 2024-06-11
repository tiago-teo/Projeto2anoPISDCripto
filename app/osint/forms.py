# '''
# Importação do módulo forms do Django.
# Este módulo contém classes e métodos para criar e manipular formulários em Django.
# '''
from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
    nome_emp = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    nome_colab = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    emails = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    passwd = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    domain = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    ipadd = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    urls = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    shodan_search = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))

    class Meta:
        model = Search
        fields = ['nome_emp', 'nome_colab', 'emails', 'passwd', 'domain', 'ipadd', 'urls', 'shodan_search']
     
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['nome_emp'].required = False
        self.fields['nome_colab'].required = False
        self.fields['emails'].required = False
        self.fields['passwd'].required = False
        self.fields['domain'].required = False
        self.fields['ipadd'].required = False
        self.fields['urls'].required = False
        self.fields['shodan_search'].required = False
# '''
# Importação do modelo Cliente.
# Importa o modelo Cliente do módulo clientes.models.
# Esse modelo representa a estrutura dos dados que serão manipulados pelo formulário.
# '''
# #from osint.models import 



# '''
# Definição da classe ClienteForm.
# Cria uma classe ClienteForm que herda de forms.ModelForm.
# Isso significa que ClienteForm é um formulário baseado no modelo Cliente.
# '''
# class ClienteForm(forms.ModelForm):
#     '''
#     Definição do campo nome:
#     forms.CharField: Define um campo de formulário do tipo CharField (campo de texto).
#     widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
#     Especifica que o campo nome deve usar um widget Textarea em vez de um campo de entrada de texto padrão.
#     Atributos rows e cols definem o tamanho do Textarea (3 linhas e 40 colunas).    
#     '''
#     nome = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))

#     '''
#     Definição do campo email:
#     forms.EmailField: Define um campo de formulário do tipo EmailField (campo de email).
#     widget=forms.EmailInput(attrs={'placeholder': 'example@domain.com'}):
#     Especifica que o campo email deve usar um widget EmailInput com um placeholder (sugestão de texto) que indica o formato esperado do email.
#     '''
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@domain.com'}))

#     '''
#     Definição do campo profissao:
#     forms.CharField: Define um campo de formulário do tipo CharField (campo de texto).
#     widget=forms.TextInput(attrs={'placeholder': 'Digite sua profissão'}):
#     Especifica que o campo profissao deve usar um widget TextInput com um placeholder que indica ao usuário que deve digitar sua profissão.
#     '''
#     profissao = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite sua profissão'}))

#     '''
#     Definição da classe interna Meta:
#     A classe Meta é usada para fornecer metadados ao formulário ModelForm.
#     '''
#     class Meta:
#         '''
#         Especificação do modelo:
#         Informa ao Django que este formulário ModelForm está vinculado ao modelo Cliente.
#         '''
#         model = Cliente

#         '''
#         Especificação dos campos: Lista os campos do modelo Cliente que devem ser incluídos no formulário.        
#         '''
#         fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']

#         '''
#         Personalização dos widgets:
#         widgets: Dicionário que permite especificar widgets personalizados para campos específicos.
#         'data_nascimento': forms.DateInput(attrs={'type': 'date'}):
#         Define que o campo data_nascimento deve usar um widget DateInput com o atributo HTML type='date', o que facilita a seleção de datas no navegador.        
#         '''
#         widgets = {
#             'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
#         }
