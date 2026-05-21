import requests

from .models import (
    Protein,
    ProteinDetail,
    ProteinPDBFile,
    ProteinSearch,
)

RCSB_SEARCH_URL = (
    "https://search.rcsb.org/rcsbsearch/v2/query"
)

RCSB_ENTRY_URL = (
    "https://data.rcsb.org/rest/v1/core/entry/{}"
)

RCSB_STRUCTURE_URL = (
    "https://www.rcsb.org/structure/{}"
)

RCSB_DOWNLOAD_URL = (
    "https://files.rcsb.org/download/{}.pdb"
)


def search_proteins(query: str) -> list:

    if not query:
        return []

    payload = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": "struct.title",
                "operator": "contains_phrase",
                "value": query,
            },
        },
        "return_type": "entry",
        "request_options": {
            "paginate": {
                "start": 0,
                "rows": 100,
            }
        },
    }

    response = requests.post(
        RCSB_SEARCH_URL,
        json=payload,
        timeout=10,
    )

    if response.status_code != 200:
        return []

    data = response.json()

    results = data.get(
        "result_set",
        [],
    )

    search = ProteinSearch.objects.create(
        query=query,
    )

    proteins = []

    for item in results:

        protein_id = item.get(
            "identifier",
        )

        protein_score = item.get(
            "score",
            0,
        )

        protein, created = (
            Protein.objects.get_or_create(
                protein_id=protein_id,
                defaults={
                    "search": search,
                    "title": (
                        f"Proteína {protein_id}"
                    ),
                    "score": protein_score,
                    "view_url": (
                        RCSB_STRUCTURE_URL.format(
                            protein_id,
                        )
                    ),
                    "download_url": (
                        RCSB_DOWNLOAD_URL.format(
                            protein_id,
                        )
                    ),
                },
            )
        )

        proteins.append(
            {
                "id": protein.protein_id,
                "score": (
                    f"Score: "
                    f"{round(protein.score, 4)}"
                ),
                "title": protein.title,
                "view_url": protein.view_url,
                "download_url": (
                    protein.download_url
                ),
            }
        )

    return proteins


def get_protein_details(
    protein_id: str,
):

    protein = Protein.objects.filter(
        protein_id=protein_id,
    ).first()

    if not protein:
        return {}

    if hasattr(
        protein,
        "details",
    ):

        details = protein.details

        return {
            "title": details.full_title,
            "classification": (
                details.classification
            ),
            "organism": (
                details.organism
            ),
            "expression_system": (
                details.expression_system
            ),
        }

    response = requests.get(
        RCSB_ENTRY_URL.format(
            protein_id,
        ),
        timeout=10,
    )

    if response.status_code != 200:
        return {}

    data = response.json()

    title = (
        data.get(
            "struct",
            {},
        ).get(
            "title",
            "Sem descrição",
        )
    )

    classification = (
        data.get(
            "struct_keywords",
            {},
        ).get(
            "pdbx_keywords",
            "Não informado",
        )
    )

    organism = "Não informado"

    expression_system = (
        "Não informado"
    )

    entities = data.get(
        "rcsb_entry_container_identifiers",
        {},
    ).get(
        "polymer_entity_ids",
        [],
    )

    if entities:

        entity_id = entities[0]

        entity_response = requests.get(
            (
                "https://data.rcsb.org/rest/v1/"
                f"core/polymer_entity/"
                f"{protein_id}/{entity_id}"
            ),
            timeout=10,
        )

        if (
            entity_response.status_code
            == 200
        ):

            entity_data = (
                entity_response.json()
            )

            organisms = entity_data.get(
                "rcsb_entity_source_organism",
                [],
            )

            if organisms:

                organism = organisms[0].get(
                    "ncbi_scientific_name",
                    "Não informado",
                )

            expression = entity_data.get(
                "rcsb_entity_host_organism",
                [],
            )

            if expression:

                expression_system = (
                    expression[0].get(
                        "ncbi_scientific_name",
                        "Não informado",
                    )
                )

    ProteinDetail.objects.create(
        protein=protein,
        classification=classification,
        organism=organism,
        expression_system=expression_system,
        full_title=title,
    )

    return {
        "title": title,
        "classification": classification,
        "organism": organism,
        "expression_system": (
            expression_system
        ),
    }


def download_pdb_file(
    protein_id: str,
):

    protein = Protein.objects.filter(
        protein_id=protein_id,
    ).first()

    if not protein:
        return None

    existing_pdb = (
        ProteinPDBFile.objects.filter(
            protein=protein,
        ).first()
    )

    if existing_pdb:
        return existing_pdb

    download_url = (
        RCSB_DOWNLOAD_URL.format(
            protein_id,
        )
    )

    response = requests.get(
        download_url,
        timeout=20,
    )

    if response.status_code != 200:
        return None

    pdb_content = response.text

    pdb_file = (
        ProteinPDBFile.objects.create(
            protein=protein,
            pdb_content=pdb_content,
        )
    )

    return pdb_file