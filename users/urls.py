from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('new_user/', views.new_user, name='new_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]