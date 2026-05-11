from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from frontend.context_processors import frontend_context

# Create your views here.
def homepage(request):                
    return render(request, 'frontend_homepage.html') 

def userpage(request): 
    if not request.user.is_authenticated:
        return redirect('account_login')

    return render(request, 'frontend_userpage.html')

def test(request):    

    return render(request, 'frontend_testpage.html') 