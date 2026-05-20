import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import search_proteins


#@login_required(login_url="/login/")
def home(request):
    return render(
        request,
        "core/home.html",
    )

@login_required(login_url="/login/")
def dashboard(request):

    query = request.GET.get("q", "")

    proteins = search_proteins(query)

    return render(
        request,
        "core/dashboard.html",
        {
            "proteins": proteins,
            "query": query,
        },
    )