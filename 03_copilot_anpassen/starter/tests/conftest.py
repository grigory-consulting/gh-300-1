from pathlib import Path

import pytest

from lager.artikel import Artikel

KOPFZEILE = "nummer;bezeichnung;lagerort;bestand;mindestbestand;sollbestand\n"


@pytest.fixture
def bestandsdatei(tmp_path: Path) -> Path:
    """Kleine Bestandsdatei mit einem knappen und einem ausreichenden Artikel."""
    pfad = tmp_path / "bestand.csv"
    pfad.write_text(
        KOPFZEILE
        + "BR-1043;Scheibenbremsbeläge gesintert;A1;4;8;24\n"
        + "KT-0900;Kette 9-fach;C1;9;5;12\n",
        encoding="utf-8",
    )
    return pfad


@pytest.fixture
def schreibe_bestand(tmp_path: Path):
    """Schreibt beliebige Datenzeilen unter die Kopfzeile und liefert den Pfad."""

    def schreiben(*zeilen: str) -> Path:
        pfad = tmp_path / "bestand.csv"
        pfad.write_text(KOPFZEILE + "".join(z + "\n" for z in zeilen), encoding="utf-8")
        return pfad

    return schreiben


@pytest.fixture
def artikelliste() -> list[Artikel]:
    """Vier Artikel, drei davon unter Mindestbestand, unsortiert."""
    return [
        Artikel("KT-1100", "Kette 11-fach", "C1", 3, 5, 12),
        Artikel("BR-1043", "Scheibenbremsbeläge gesintert", "A1", 4, 8, 24),
        Artikel("KT-0900", "Kette 9-fach", "C1", 9, 5, 12),
        Artikel("ZG-0020", "Bremszug Edelstahl 1700 mm", "C3", 0, 10, 40),
    ]
