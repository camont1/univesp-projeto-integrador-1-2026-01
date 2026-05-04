# univesp-projeto-integrador-1-2026-01
Repositório dedicado ao desenvolvimento do projeto da disciplina do Projeto Integrador 1 da UNIVESP

## Acesso provisório do SuperUsuário:
username = PI01
senha = 20260103

## Instalação das Dependências (Ambiente Virtual)
O estado atual do repositório está configurado com o Python 3.12, portanto, prefira usar esta versão para evitar problemas de compatibilidade. 

Porém, já realisei testes da aplicação em outro ambiente com o Phyton 3.14 e funcionou sem nenhum problema.

### DJANGO (versão 6.0.4):

    uv pip install django

## Outras dependências

### Blibliotecas do Python : 

    uv pip install requests

### Plugns do Django:

    uv pip install django-bootstrap5  django-allauth "django-allauth[socialaccount]" "django-allauth[headless]"

Documentação dos recursos utilizados. Consulte caso tenha alguma dúvida:

https://docs.astral.sh/uv/

https://django-bootstrap5.readthedocs.io/en/latest/

https://docs.allauth.org/en/latest/index.html

https://requests.readthedocs.io/en/latest/


## Informações sobre a aplicação:

Conforme definido no escopo do projeto (que será utlizado o django templates para a construção do frontend), foi adicionado o bootstrap5 para utlização dos estilos padrão.

Com o mesmo objetivo, também foi adicionado um pack de icones na pasta /static.

Para cumprir com os requisitos da Etapa 1 do projeto, foi adicionado plugin allauth do django, para dar melhores recursos de autenticação de usuários. 


### Estrutura do projeto:

Além da app do projeto, nomeada 'core', foram criados duas outras app's com os seguintes objetivos:

#### 'frontend' 

Converge os templates de layout das páginas (frontend_homecontent.html e frontend_usercontent.html), além da página base (frontend_base.html) que define o HEAD e demais elementos fixos e comuns para as páginas de layouts. 

Ainda na app 'frontend' foi adicionado um processador de variáveis globais (context_processors.py) com o objetivo de definir os templates de aplicação que são incluídos nas páginas de layout a partir da TAG 'include'. Esta foi a solução encontrada para permitir a integração do allauth sem modificar as suas views. Portanto, o fluxo de desenvolviento proposto é: 

1. as views chamam os templates de layout a partir do método 'render()'; 
ex:

    def test(request):   
        # lógica da view
        return render(request, 'frontend_testpage.html') 

2. os templates de apps são retornados pela função 'frontend_context()';
ex:

    else:
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'app1_index.html',
                'SIDE': 'app2_menu.html',
                'TOP': 'app3_toggle.html',
            }
        }

    return frontend  

3. o template de layout renderizados na view exibe os templates de apps definidos a partir da TAG 'include';
ex:

    <center> {% include TEMPLATES.TOP %}  </center>

    <center> {% include TEMPLATES.SIDE%}  </center>

    <center> {% include TEMPLATES.CONTENT %}  </center>


#### 'users'

Responsável por integrar as funcionalidade do 'allauth', contendo os templantes de substituição as views necessárias que não são definidas por padrão pelo allauth. 

ATENÇÃO: devido à solução de integração do allauth desenvolvida, verificou-se uma incompatibildiade do uso do decorator '@loguin_required', pois o seu redirecionamento não atualiza as variáveis definidas pela função 'frontend_context()'. Felizmente, a solução é simples, bastando utilizar no lugar o método redirect.
ex:

    # @login_required # não utilizar
    def profile(request):

        if not request.user.is_authenticated:
            return redirect('account_login')  # use este controle no lugar.


### Estrutura de templates:

Com o objetivo de facilitar o desenvolviemnto do frontend da aplicação optou-se por utilizar a menor quantidade de TAGS possível nos templates, possibilitando que as páginas possam ser criadas e editadas com o uso de qualquer editor HTML.