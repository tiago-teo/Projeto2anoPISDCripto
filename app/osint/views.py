from django.shortcuts import render, get_object_or_404, redirect
#from .services import cliente_services
# from .entidades import cliente
from .models import Search, Result
# from .forms import ClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from perfis.models import Perfil
from .forms import SearchForm
import time, json, os, dns.resolver, requests, shodan
from . import intelxapi
from index.encrypt import decrypt
from googlesearch import search as searching
import time
# Create your views here.

#View para exibir o formulário de pesquisa
@login_required(login_url='index')
def search_form(request, pk):
    #Obtém o perfil do utilizador autenticado pelo ID(pk)
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            messages.success(request, 'Searching...')
            
            #Obtém os dados do formulário
            email = form.cleaned_data['emails']
            domain = form.cleaned_data['domain']
            nome_emp = form.cleaned_data['nome_emp']
            shodan_search = form.cleaned_data['shodan_search']
            gdork = form.cleaned_data['google_dork']
            
            #-------------------------------------------------------INTELX-----------------------------------------------------------------
            # Faz a requisição à API "IntelX"
            if perfil.intelx_api is not None and perfil.intelx_api!="":
                intelx_api_key = decrypt(perfil.intelx_api)
                intelx = intelxapi.intelx(intelx_api_key)
                # --------------------------------------Email Results------------------------------

                try:
                    
                    search_response_email = intelx.search(email, maxresults=10)
                    print(f"Search Response: {search_response_email}")

                        
                    email_results = [record['name'] for record in search_response_email.get('records', []) if 'name' in record]
                    print(f"Extracted Names: {email_results}")
                    save_result = json.dumps(email_results)
                    
                    
                    

                except Exception as e:
                    print(f"An error occurred: {e}")
                    email_results = ""
                    save_result = json.dumps(email_results)
                #---------------------------------------Domain Results----------------------------

                try:
                    
                    search_response_domain = intelx.search(domain, maxresults=10)
                    print(f"Search Response: {search_response_domain}")

                        
                    domain_results = [record['name'] for record in search_response_domain.get('records', []) if 'name' in record]
                    print(f"Extracted Names: {domain_results}")
                    save_result_domain = json.dumps(domain_results)
                    
                except Exception as e:
                    print(f"An error occurred: {e}")
                    domain_results = ""
                    save_result_domain = json.dumps(domain_results)

            else:
                email_results = ""
                save_result = json.dumps(email_results)
                domain_results = ""
                save_result_domain = json.dumps(domain_results)


            #-------------------------------------------------------HUNTER.IO-----------------------------------------------------------------
            # Hunter.io API key
            if perfil.hunter_api is not None and perfil.hunter_api!="":
                HUNTER_API_URL = 'https://api.hunter.io/v2/domain-search'
                HUNTER_API_KEY = decrypt(perfil.hunter_api)
                #------------------------------------Hunter.io-------------------------------------

                try:
                    params = {
                        'company': nome_emp,
                        'api_key': HUNTER_API_KEY
                    }
                    response = requests.get(HUNTER_API_URL, params=params)                
                    r = response.json()
                    emp_result = r.get('data', {}).get('emails', [])
                    emp_result_save = json.dumps(emp_result)

                except Exception as e:
                    print(f"Ocorreu um erro: {e}")
                    emp_result=[]
                    emp_result_save = json.dumps(emp_result)
            else:
                emp_result=[]
                emp_result_save = json.dumps(emp_result)

            #-------------------------------------------------------SHODAN-----------------------------------------------------------------
            # Shodan API Key
            if perfil.shodan_api is not None and perfil.shodan_api!="":
                SHODAN_API_KEY = decrypt(perfil.shodan_api)
                #-----------------------------------Shodan------------------------------------------
                api = shodan.Shodan(SHODAN_API_KEY)
                account_info = api.info()
                msg = "[+] Available Shodan query credits: %d" % account_info.get('query_credits')
                print(msg)
                try: 
                    shodan_result = api.search(shodan_search)
                    
                except shodan.APIError as e:
                    print(f"Ocorreu um erro: {e}")
                    shodan_result=[]
            
            else:
                shodan_result = []

            
            #----------------------------------------------------------SPF------------------------------------------------------------------
            try:
                respostas = dns.resolver.resolve(domain, 'TXT')
        
                # Armazena os resultados em uma lista
                spf_result = []
                for rdata in respostas:
                    for txt_string in rdata.strings:
                        decoded_string = txt_string.decode()
                        # Verifica se o registro contém informações SPF
                        if decoded_string.startswith("v=spf1"):
                            spf_result.append(decoded_string)
                spf_result_save = json.dumps(spf_result)
                
                
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                spf_result=[]
                spf_result_save = json.dumps(spf_result)
            
            
            #-------------------------------------------------------------Google Dorks-------------------------------------------------
            try:
                dork = gdork
                amount = 15

                requ = 0
                counter = 0
                dork_results = []
                for results in searching(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
                    counter = counter + 1                    
                    dork_results.append(results)
                    dork_result_save = json.dumps(dork_results)
                    time.sleep(0.1)
                    requ += 1
                    if requ >= int(amount):
                        break                    
                    time.sleep(0.1)

            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                dork_result=[]
                dork_result_save = json.dumps(dork_result)
            
            #Criação dos Resuldados e renderiza a página de resultados
            new = Result.objects.create(search=search, domain_leak=save_result_domain, email_leak=save_result, spf=spf_result_save, emp=emp_result_save, shodan=shodan_result, dork=dork_result_save)
            return render(request, 'results.html', {'email_results': email_results, 'domain_results': domain_results, 'spf': spf_result, 'emp_result': emp_result, 'shodan_result': shodan_result, 'dork_result': dork_results, 'email': email, 'domain': domain, 'emp': nome_emp, 'shodan': shodan_search, 'gdork': gdork, 'user': request.user, 'perfil': perfil})
            
    else:
        form = SearchForm()
    return render(request, 'form_search.html', {'user': request.user, 'form': form, 'perfil': perfil})



#View para exibir os resultados da pesquisa
@login_required(login_url='index')
def results(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    return render(request, 'results.html', {'user': request.user, 'perfil': perfil})


#View para exibir o histórico de pesquisa do utilizador
@login_required(login_url='index')
def history(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    search = Search.objects.all()
    return render(request, 'history.html', {'user': request.user, 'perfil': perfil, 'search': search})


#View para exibir os resultados detalhados de uma pesquisa em específico do histórico
@login_required(login_url='index')
def history_results(request, pk, id):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    search = get_object_or_404(Search, id=id)
    results_model = get_object_or_404(Result, search_id=id)
    jsonDec = json.decoder.JSONDecoder()
    email_results = jsonDec.decode(results_model.email_leak)
    domain_results = jsonDec.decode(results_model.domain_leak)
    spf_result = jsonDec.decode(results_model.spf)
    emp_results = jsonDec.decode(results_model.emp)
    shodan_result = jsonDec.decode(results_model.shodan)
    dork_results = jsonDec.decode(results_model.dork)
    return render(request, 'results.html', {'email_results': email_results, 'domain_results': domain_results, 'spf': spf_result, 'emp_result': emp_results, 'shodan_result': shodan_result, 'dork_result': dork_results, 'email':search.emails, 'domain':search.domain, 'emp': search.nome_emp, 'shodan': search.shodan_search, 'gdork': search.google_dork, 'user': request.user, 'perfil': perfil, 'search': search})

