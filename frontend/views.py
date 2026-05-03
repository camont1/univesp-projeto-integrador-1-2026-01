from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):

    # criando um dicionário com os templates que serão incluídos no userpage.html.
    templates = {
        'content': 'frontend_homecontent.html',
    }

    return render(request, 'frontend_homepage.html', {'templates': templates})

@login_required(login_url='login')
def userpage(request):

    # criando um dicionário com os templates que serão incluídos no userpage.html.
    templates = {
        'content': 'frontend_usercontent.html',
    }
    return render(request, 'frontend_userpage.html', {'templates': templates})