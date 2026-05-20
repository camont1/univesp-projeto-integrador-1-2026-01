from django.contrib import admin
from django.urls import include, path

from apps.users.views import login_view


urlpatterns = [

    path(
        "",
        include("apps.core.urls"),
    ),

    path(
        "users/",
        include("apps.users.urls"),
    ),

    path(
        "login/",
        login_view,
        name="login",
    ),

    path(
        "admin/",
        admin.site.urls,
    ),
]