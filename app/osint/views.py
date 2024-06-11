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

# Create your views here.

@login_required(login_url='index')
def search_form(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            messages.success(request, 'Searching...')
            email = form.cleaned_data['emails']
            domain = form.cleaned_data['domain']
            nome_emp = form.cleaned_data['nome_emp']
            shodan_search = form.cleaned_data['shodan_search']
            
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

            
            #--------------------------------------SPF--------------------------------------
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
            
            

            new = Result.objects.create(search=search, domain_leak=save_result_domain, email_leak=save_result, spf=spf_result_save, emp=emp_result_save, shodan=shodan_result)
            return render(request, 'results.html', {'email_results': email_results, 'domain_results': domain_results, 'spf': spf_result, 'emp_result': emp_result, 'shodan_result': shodan_result, 'email': email, 'domain': domain, 'emp': nome_emp, 'shodan': shodan_search, 'user': request.user, 'perfil': perfil})
            
    else:
        form = SearchForm()
    return render(request, 'form_search.html', {'user': request.user, 'form': form, 'perfil': perfil})


@login_required(login_url='index')
def results(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    return render(request, 'results.html', {'user': request.user, 'perfil': perfil})

@login_required(login_url='index')
def history(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    perfis = Perfil.objects.all()
    search = Search.objects.all()
    return render(request, 'history.html', {'user': request.user, 'perfil': perfil, 'search': search})

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
    return render(request, 'results.html', {'email_results': email_results, 'domain_results': domain_results, 'spf': spf_result, 'emp_result': emp_results, 'shodan_result': shodan_result, 'email':search.emails, 'domain':search.domain, 'emp': search.nome_emp, 'shodan': search.shodan_search, 'user': request.user, 'perfil': perfil, 'search': search})

