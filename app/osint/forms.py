
from django import forms
from .models import Search

#Class SearcForm que importa um modelo de formulário
#Define também os campos do formulário com widgets personalizados para texto
class SearchForm(forms.ModelForm):
    nome_emp = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    nome_colab = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    emails = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    passwd = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    domain = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    ipadd = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    urls = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    shodan_search = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))
    google_dork = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':1}))

#Define o modelo associado aos campos que serão utilizados no formulário
    class Meta:
        model = Search
        fields = ['nome_emp', 'nome_colab', 'emails', 'passwd', 'domain', 'ipadd', 'urls', 'shodan_search', 'google_dork']
     
#Define que nenhum campo é obrigatório, caso o utilizador queira só pesquisar por um dos campos do formulário
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
        self.fields['google_dork'].required = False
