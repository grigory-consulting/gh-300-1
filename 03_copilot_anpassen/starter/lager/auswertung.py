"""Auswertungen über den Lagerbestand."""

from lager.artikel import Artikel


def unter_mindestbestand(artikel: list[Artikel]) -> list[Artikel]:
    """Artikel, deren Bestand unter dem Mindestbestand liegt, nach Lagerort und Nummer sortiert."""
    knapp = [a for a in artikel if a.bestand < a.mindestbestand]
    return sorted(knapp, key=lambda a: (a.lagerort, a.nummer))


def bestellmenge(artikel: Artikel) -> int:
    """Stückzahl, die bis zum Sollbestand fehlt.

    Liegt der Bestand nicht unter dem Mindestbestand, wird nichts bestellt (0).
    """
    if artikel.bestand >= artikel.mindestbestand:
        return 0
    return artikel.sollbestand - artikel.bestand
