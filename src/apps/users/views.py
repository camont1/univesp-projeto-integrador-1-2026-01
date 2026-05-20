from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import RegisterForm, LoginForm

def logout_view(request):

    logout(request)

    return redirect("/")


def register(request):

    error = None

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]

            if User.objects.filter(username=email).exists():

                error = "Usuário já existe."

            else:

                User.objects.create_user(
                    username=email,
                    email=email,
                    password=form.cleaned_data["password"],
                    first_name=form.cleaned_data["name"],
                )

                return redirect("/")

    else:

        form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form,
            "error": error,
        },
    )

def login_view(request):

    error = None

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]

            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=email,
                password=password,
            )

            if user is not None:

                login(request, user)

                return redirect("/dashboard/")

            else:

                error = "Email ou senha inválidos."

    else:

        form = LoginForm()

    return render(
        request,
        "users/login.html",
        {
            "form": form,
            "error": error,
        },
    )