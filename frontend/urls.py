from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('userpage/', views.userpage, name='userpage'),
    path("test/", views.test, name="test"),
]