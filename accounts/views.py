from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ProfileForm

@login_required(login_url='login')
def profile(request):
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
            return render(request, 'profile.html', {'form': form, 'errors': errors})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm(User.objects.get(username=request.user.username).__dict__)        
        return render(request, "profile.html", {"form": form})

def new_user(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)

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

                login(request, user)            
                return redirect('userpage')
        else:
            # Retorna o dicionário dos erros de validação do formulário, caso existam. 
            # Se o dicionário estiver vazio, significa que o formulário é válido.
            errors = form.errors.as_data()
            return render(request, 'profile.html', {'form': form, 'error': errors})
        
    else:
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            # if a GET (or any other method) we'll create a blank form
            form = ProfileForm()
            return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            form = ProfileForm()
            return render(request, 'login.html', {'error': 'Invalid username or password', 'form': form})
    else:
        if request.user.is_authenticated:
            return redirect('userpage')
        else:
            form = ProfileForm()
            return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)       
    return redirect('home')