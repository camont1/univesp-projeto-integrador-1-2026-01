from django.urls import path

from .views import (
    dashboard,
    export_pdb,
    home,
    protein_details,
    saved_proteins
)

urlpatterns = [

    path(
        "",
        home,
        name="home",
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard",
    ),

    path(
        "protein-details/<str:protein_id>/",
        protein_details,
        name="protein_details",
    ),

    path(
        "export/<str:protein_id>/",
        export_pdb,
        name="export_pdb",
    ),

    path(
        "dashboard/proteins/",
        saved_proteins,
        name="saved_proteins",
    ),
]