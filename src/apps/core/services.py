import requests


RCSB_SEARCH_URL = (
    "https://search.rcsb.org/rcsbsearch/v2/query"
)

RCSB_STRUCTURE_URL = (
    "https://www.rcsb.org/structure/{}"
)

RCSB_DOWNLOAD_URL = (
    "https://files.rcsb.org/download/{}.pdb"
)
# 
def search_proteins(query: str) -> list:
# 
    if not query:
        return []
# 
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
                "rows": 10,
            }
        },
    }
# 
    response = requests.post(
        RCSB_SEARCH_URL,
        json=payload,
        timeout=10,
    )
# 
    if response.status_code != 200:
        return []
# 
    data = response.json()
# 
    results = data.get(
        "result_set",
        [],
    )
# 
    proteins = []
# 
    for item in results:
        protein_id = item.get("identifier")
        protein_score = item.get("score")
        proteins.append(
            {
                "id": protein_id,
                "score": f"Score: {round(protein_score, 4)}",
                "title": (
                    f"Proteína {protein_id}"
                ),
                "description": (
                    "Resultado encontrado no RCSB Protein Data Bank."
                ),
                "view_url": (
                    RCSB_STRUCTURE_URL.format(
                        protein_id
                    )
                ),
                "download_url": (
                    RCSB_DOWNLOAD_URL.format(
                        protein_id
                    )
                ),
            }
        )
    return proteins