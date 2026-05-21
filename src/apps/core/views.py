from django.contrib.auth.decorators import (
    login_required,
)

from django.contrib import messages
from django.db.models import Q

from django.core.paginator import (
    Paginator,
)

from django.http import JsonResponse

from django.shortcuts import (
    redirect,
    render,
)

from .models import Protein

from .services import (
    download_pdb_file,
    get_protein_details,
    search_proteins,
)


def home(request):

    return render(
        request,
        "core/home.html",
    )


@login_required(login_url="/login/")
def dashboard(request):

    query = request.GET.get(
        "q",
        "",
    )

    proteins = search_proteins(
        query,
    )

    paginator = Paginator(
        proteins,
        20,
    )

    page_number = request.GET.get(
        "page",
    )

    page_obj = paginator.get_page(
        page_number,
    )

    return render(
        request,
        "core/dashboard.html",
        {
            "proteins": page_obj,
            "query": query,
            "page_obj": page_obj,
        },
    )


@login_required(login_url="/login/")
def protein_details(
    request,
    protein_id,
):

    details = get_protein_details(
        protein_id,
    )

    return JsonResponse(
        details,
    )


@login_required(login_url="/login/")
def export_pdb(
    request,
    protein_id,
):

    pdb_file = download_pdb_file(
        protein_id,
    )

    if pdb_file:

        messages.success(
            request,
            (
                f"Arquivo PDB "
                f"{protein_id} "
                f"salvo com sucesso."
            ),
        )

    else:

        messages.error(
            request,
            (
                f"Erro ao salvar "
                f"arquivo PDB "
                f"{protein_id}."
            ),
        )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/dashboard/",
        )
    )


@login_required(login_url="/login/")
@login_required(login_url="/login/")
def saved_proteins(request):

    query = request.GET.get(
        "q",
        "",
    )

    proteins = (
        Protein.objects
        .select_related(
            "details",
            "pdb_file",
            "search",
        )
        .order_by("-created_at")
    )

    if query:

        proteins = proteins.filter(

            Q(
                protein_id__icontains=query,
            )

            |

            Q(
                search__query__icontains=query,
            )

            |

            Q(
                details__full_title__icontains=query,
            )

        ).distinct()

    return render(
        request,
        "core/saved_proteins.html",
        {
            "proteins": proteins,
            "query": query,
        },
    )