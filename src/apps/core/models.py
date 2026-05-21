from django.db import models


class ProteinSearch(models.Model):

    query = models.CharField(
        max_length=255,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.query


class Protein(models.Model):

    protein_id = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
    )

    search = models.ForeignKey(
        ProteinSearch,
        on_delete=models.CASCADE,
        related_name="proteins",
    )

    title = models.CharField(
        max_length=500,
    )

    score = models.FloatField(
        default=0,
    )

    view_url = models.URLField()

    download_url = models.URLField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.protein_id


class ProteinDetail(models.Model):

    protein = models.OneToOneField(
        Protein,
        to_field="protein_id",
        db_column="protein_id",
        on_delete=models.CASCADE,
        related_name="details",
    )

    classification = models.CharField(
        max_length=255,
        blank=True,
    )

    organism = models.CharField(
        max_length=255,
        blank=True,
    )

    expression_system = models.CharField(
        max_length=255,
        blank=True,
    )

    full_title = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return (
            f"{self.protein.protein_id} - "
            f"{self.classification}"
        )

class ProteinPDBFile(models.Model):

    protein = models.OneToOneField(
        Protein,
        to_field="protein_id",
        db_column="protein_id",
        on_delete=models.CASCADE,
        related_name="pdb_file",
    )

    pdb_content = models.TextField()

    downloaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return (
            f"PDB - "
            f"{self.protein.protein_id}"
        )