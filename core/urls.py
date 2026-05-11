"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from users import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path ('', include('frontend.urls')),
    path ('accounts/profile/', views.profile, name='profile'),
    path('frontend/', include('frontend.urls')),
    path("users/", include("users.urls")),
    path('admin/', admin.site.urls),

    # Even when using headless, the third-party provider endpoints are stil
    # needed for handling e.g. the OAuth handshake. The account views
    # can be disabled using `HEADLESS_ONLY = True`.
    path("accounts/", include("allauth.urls")),

    # Include the API endpoints:
    path("_allauth/", include("allauth.headless.urls")),
]
