# Safe Search - We know what the internet knows about you

## Introdução

No âmbito das unidades curriculares de Criptografia, Sistemas Distribuidos e Segurança, e Programação para a Internet, foi proposto um projeto onde o tema escolhido pelo grupo foi um sistema de pesquisa de informação online, capaz de pesquisar informação de diversos dados em diversas fontes, centralizando os resultados.

Para a realização deste projeto utilizamos os seguintes componentes: Django + Docker Compose + Nginx + gunicorn + mysql + djangobootstrap

O seguinte documento indica o processo de instalação e possível uso.


## Requerimentos

### Gerais

1. IntelX API Key: https://intelx.io/
2. Hunter API Key: https://hunter.io/
3. Shodan API key: https://www.shodan.io/

### Linux

1. Instalar docker: apt-get install docker
2. Instalar docker-compose: apt-get install docker-compose
3. Instalar git: apt-get install git
4. Instalar VsCode(Code-OSS) com a extenção mysql. (Opcional) *

*\* Caso queira ver o código e/ou fazer alterações

### Windows

1. Instalar docker desktop (É necessario WSL)
2. Instalar git
3. Instalar VsCode com a extenção mysql. (Opcional) *



## Instalação

1. Criar uma pasta para o projeto 
2. Num terminal navegar até essa pasta (Ex: cd projeto/ )
3. Executar git clone http... *COLOCAR ENDEREÇO*
4. cd Projeto2anoPISDCripto/app/
5. criar o ficheiro .env (ver o .env-example) Nota: A Secret Key deve ter no minimo 32 caracteres
6. cd . . (Voltar para a pasta Projeto2anoPISDCripto)
7. Executar: docker compose up --build -d
8. Executar: docker compose exec app python manage.py migrate
9. Executar: docker compose exec app python manage.py collectstatic
10. Navegar para  "https://localhost". No navegador firefox basta pesquisar "localhost", caso não funcione é preciso pesquisar exatamente "https://localhost". Poderá aparecer uma mensagem de indicação que o site não é segura devido ao facto que o certificado SSL não foi assinnado por uma autoridade de certificação de confiança. Caso esta mensagem apareça, basta carregar em "avançado" e "prosseguir na mesma".

Caso tenha o VsCode instalado basta abrir este mesmo na pasta criada para este sistema (passo 1) e no próprio VsCode em Terminal -> New Terminal, criar um novo terminal e executar os passos do 3 ao 10.


## Utilização do sistema

1. Navegar na página principal e nas páginas "service" e "about"
2. Registar utilizador em "Sign Up" na página principal. Após o registo será redirecinado para a página "Sign In"
3. (Alternativa se o utilizador ja estava criado) Fazer Login do utilizador em "Log In" na página principal. Após o login será redirecionado para a página principal do sistema.
4. Carregar na foto no canto superior da página e carregar em perfil para navegar para o perfil.
5. No perfil preencher com uma foto, nome (caso queira mudar o "username"), e preencher as API keys. Após preencher carregar em submeter
6. No menu lateral na parte esquerda da página, carregar em "Procurar Informação" -> "Pesquisa".
7. Preencher o formulário de pesquisa nos campos "Nome Emp", "Emails", "Domain", "Shodan Search" (Se a API for grátis no caso do Shodan, não irá obter nenhum resultado pois é preciso uma chave paga). Submeter o formulario e será redirecionado para a página com os resultados. Os restantes campos não foram configurados pois o uso de certas ferramentas é pago e não foi possivel utilizar esses mesmos campos.
8. No menu lateral na parte esquerda da página, carregar em "Procurar Informação" -> "Histórico de Pesquisa". Nesta secção poderá observar o historico das pesquisas feitas. Ao carregar em results será redirecionado para o resultado obtido de cada pesquisa.



## Utilização do VsCode (MySQL)

1. Abrindo o VsCode e tendo a extenção MySQL instalada, carregar no icon da base de dados na barra lateral à esquerda
2. Carregar em "Criar Conexão"
3. Colocar em "Password": "root", em "Database": "app_db". Caso não funcione pode significar que existe outro serviço que esteja a ocupar a porta 3306 (Por exemplo um serviço mysql ja instalado no dispositivo), e será necessário parar esse serviço para inicar a conexão.
4. Após a conexão iniciada, do lado esquerdo deverá aparecer a base de dados com as suas tabelas, onde poderá navegar entre elas, sendo as mais relevantes as tabelas: "Auth_user" (Tabela com informações referente ao utilizador (password e username)), "perfis_perfil" (Tabela com informações referente ao perfil(foto e api_keys)), "osint_search"(Tabela com informações referente aos dados pesquisados ) e "osint_result"(Tabela com informações referente aos resultados dos dados pesquisados).



## TroubleShooting

- Mysql
	- Caso não funcione pode significar que existe outro serviço que esteja a ocupar a porta 3306 (Por exemplo um serviço mysql ja instalado no dispositivo), e será necessário parar esse serviço para inicar a conexão.
	
- Pesquisa de informação
	- Confirmar que no perfil foram submetidas **todas** as API Keys
	
- Outros:
	- Mudar no ficheiro ".env" em /app/: DEBUG: True
	- Reiniciar os conteiners:
		1. Na linha de comandos executar: docker compose down (para remover o conteiner além de o parar)
		2. E executar: docker compose up --build -d
	- Repetir o que causou o erro e observar as informações referentes ao erro.