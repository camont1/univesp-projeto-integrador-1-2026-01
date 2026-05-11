from django.http import HttpRequest

def frontend_context(request, ctl=None):
    """
    Context processor for frontend app.
    """       

    if not ctl:
        caminho = HttpRequest
        ctl = caminho.get_full_path_info(request)

    if ctl == '/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'frontend_homedefault.html',
            }
        }
    elif ctl == '/accounts/password/change/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_password_change.html',
            }
        } 
    elif ctl == '/accounts/3rdparty/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_connections.html',
            }
        } 
    elif ctl == '/accounts/email/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_email.html',
            }
        }           
    elif ctl == '/accounts/password/reset/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_password_reset.html',
            }
        }       
    elif ctl == '/accounts/sessions/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_usersession_list.html',
            }
        }          
    elif ctl == '/frontend/test/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'frontend_testdefault.html',
            }
        }
    elif ctl == '/frontend/userpage/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'frontend_userdefault.html',
            }
        }        
    elif ctl == '/accounts/login/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_login.html',
            }
        }
    elif ctl == '/accounts/logout/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_logout.html',
            }
        }        
    elif ctl == '/accounts/signup/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_signup.html',
            }
        }        
    elif ctl == '/accounts/profile/':
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'users_profile.html',
            }
        }
    else:
        frontend = {
            'TEMPLATES': {
                'CONTENT': 'frontend_basedefault.html',
            }
        }

    return frontend  