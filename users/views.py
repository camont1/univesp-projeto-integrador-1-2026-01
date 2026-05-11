from wsgiref import headers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ProfileForm, NewUserForm
from allauth.account.forms import LoginForm
from frontend.context_processors import frontend_context

# @login_required () ## não utilizar
def profile(request):

    if not request.user.is_authenticated:
        return redirect('account_login')  # usar esse controle no lugar.

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # salvar as alterações no perfil do usuário
            user = User.objects.get(username=request.user.username)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']            
            user.save()
            # redirect to a new URL:            
            return redirect('userpage')
        else:
            # Retorna o dicionário dos erros de validação do formulário, caso existam. 
            # Se o dicionário estiver vazio, significa que o formulário é válido.
            errors = form.errors.as_data() 
            return render(request, 'frontend_userpage.html', {'form': form, 'errors': errors})
    
    else:
        form = ProfileForm(User.objects.get(username=request.user.username).__dict__)          
        return render(request, "frontend_userpage.html", {"form": form})

def new_user(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewUserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():            

            #process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()   
            return redirect('account_login')
                
        else:
            # Retorna o dicionário dos erros de validação do formulário, caso existam. 
            # Se o dicionário estiver vazio, significa que o formulário é válido.
            errors = form.errors.as_data()
            return render(request, 'frontend_userpage.html', {'form': form, 'errors': errors})
        
    else:
        if request.user.is_authenticated:            
            return redirect('profile')
        else:
            # if a GET (or any other method) we'll create a blank form
            form = NewUserForm()
            return render(request, 'frontend_userpage.html', {'form': form})
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm

        if form.clean:                
            form.login(request.POST) 
            # criando um dicionário com os templates que serão incluídos no userpage.html.
            return redirect('profile')
                 
        else:
            errors = form.errors.as_data()  # Retorna o dicionário dos erros de validação do formulário, caso existam. Se o dicionário estiver vazio, significa que o formulário é válido.
            # criando um dicionário com os templates que serão incluídos no userpage.html.
            return render(request, 'frontend_userpage.html', {'form': form, 'errors': errors})
        
    else:        
        if request.user.is_authenticated:
            return redirect('userpage')
        
        else:
            form = LoginForm()
            return render(request, 'frontend_userpage.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)       
    return redirect('homepage')