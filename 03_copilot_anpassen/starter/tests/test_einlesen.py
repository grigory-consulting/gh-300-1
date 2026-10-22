import logging
from pathlib import Path

import pytest

from lager.einlesen import lade_bestand


def test_liest_alle_artikel_mit_mengen(bestandsdatei: Path) -> None:
    artikel = lade_bestand(bestandsdatei)

    assert [a.nummer for a in artikel] == ["BR-1043", "KT-0900"]
    assert artikel[0].bestand == 4
    assert artikel[0].mindestbestand == 8
    assert artikel[0].sollbestand == 24


def test_umlaute_bleiben_erhalten(bestandsdatei: Path) -> None:
    artikel = lade_bestand(bestandsdatei)

    assert artikel[0].bezeichnung == "Scheibenbremsbeläge gesintert"


def test_zeile_ohne_nummer_wird_mit_warnung_uebersprungen(schreibe_bestand, caplog) -> None:
    pfad = schreibe_bestand(";Ohne Nummer;A1;1;1;1", "KT-0900;Kette 9-fach;C1;9;5;12")

    with caplog.at_level(logging.WARNING):
        artikel = lade_bestand(pfad)

    assert [a.nummer for a in artikel] == ["KT-0900"]
    assert "Zeile 2" in caplog.text


def test_fehlende_datei_meldet_pfad(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="Bestandsdatei nicht gefunden"):
        lade_bestand(tmp_path / "gibt_es_nicht.csv")


def test_keine_zahl_meldet_datei_zeile_und_wert(schreibe_bestand) -> None:
    pfad = schreibe_bestand("KT-0900;Kette 9-fach;C1;neun;5;12")

    with pytest.raises(ValueError, match=r"bestand.csv, Zeile 2: 'neun' in Spalte bestand"):
        lade_bestand(pfad)


def test_negativer_bestand_wird_abgelehnt(schreibe_bestand) -> None:
    pfad = schreibe_bestand("KT-0900;Kette 9-fach;C1;-1;5;12")

    with pytest.raises(ValueError, match="darf nicht negativ sein"):
        lade_bestand(pfad)


def test_sollbestand_unter_mindestbestand_wird_abgelehnt(schreibe_bestand) -> None:
    pfad = schreibe_bestand("KT-0900;Kette 9-fach;C1;9;12;5")

    with pytest.raises(ValueError, match="Sollbestand 5 liegt unter Mindestbestand 12"):
        lade_bestand(pfad)


def test_fehlende_spalte_wird_benannt(tmp_path: Path) -> None:
    pfad = tmp_path / "bestand.csv"
    pfad.write_text("nummer;bezeichnung;lagerort;bestand\nKT-0900;Kette;C1;9\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Spalten fehlen: mindestbestand, sollbestand"):
        lade_bestand(pfad)
