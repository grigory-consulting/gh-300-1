"""Datenmodell für einen Lagerartikel."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Artikel:
    """Ein Artikel im Ersatzteillager.

    Mengen sind Stückzahlen. Fällt der Bestand unter den Mindestbestand,
    wird bis zum Sollbestand nachbestellt.
    """

    nummer: str
    bezeichnung: str
    lagerort: str
    bestand: int
    mindestbestand: int
    sollbestand: int
