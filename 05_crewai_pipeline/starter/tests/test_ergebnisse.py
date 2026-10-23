"""Prüft die Ergebnisdateien der Pipeline gegen die Werte, die in den Rechnungen stehen.

Die Tests lesen ergebnis/<rechnung>.json. Fehlt eine Datei, wird der Test übersprungen.
"""

import json
from pathlib import Path

import pytest

ERGEBNIS = Path(__file__).resolve().parent.parent / "ergebnis"

SOLL = {
    "rechnung_1": {
        "absender": "Fahrradteile Nord GmbH",
        "rechnungsnummer": "RE-2026-0815",
        "rechnungsdatum": "2026-10-14",
        "betrag_netto": 207.70,
        "umsatzsteuer": 39.46,
        "betrag_brutto": 247.16,
        "positionen": [
            ("Kette 11-fach", 3, 89.70),
            ("Bremszug Edelstahl 1700 mm", 40, 118.00),
        ],
    },
    "rechnung_2": {
        "absender": "Werkstattbedarf Süd AG",
        "rechnungsnummer": "2026-4711",
        "rechnungsdatum": "2026-10-02",
        "betrag_netto": 1234.50,
        "umsatzsteuer": 234.56,
        "betrag_brutto": 1469.06,
        "positionen": [
            ("Montageständer Profi", 2, 578.00),
            ("Drehmomentschlüssel 5-25 Nm", 1, 149.90),
            ("Werkstattwagen 7 Schubladen", 1, 506.60),
        ],
    },
}


def lade(name: str) -> dict:
    datei = ERGEBNIS / f"{name}.json"
    if not datei.exists():
        pytest.skip(f"{datei.name} fehlt: erst python pipeline.py rechnungen/{name}.pdf ausführen")
    return json.loads(datei.read_text(encoding="utf-8"))


@pytest.mark.parametrize("name", SOLL)
def test_kopfdaten(name):
    ist, soll = lade(name), SOLL[name]
    assert ist["absender"] == soll["absender"]
    assert ist["rechnungsnummer"] == soll["rechnungsnummer"]
    assert ist["rechnungsdatum"] == soll["rechnungsdatum"]


@pytest.mark.parametrize("name", SOLL)
def test_betraege(name):
    ist, soll = lade(name), SOLL[name]
    for feld in ("betrag_netto", "umsatzsteuer", "betrag_brutto"):
        assert ist[feld] == pytest.approx(soll[feld], abs=0.005), feld


@pytest.mark.parametrize("name", SOLL)
def test_positionen(name):
    ist, soll = lade(name), SOLL[name]
    gefunden = [(p["bezeichnung"], p["menge"], p["betrag"]) for p in ist["positionen"]]
    assert len(gefunden) == len(soll["positionen"])
    for (b_ist, m_ist, e_ist), (b_soll, m_soll, e_soll) in zip(gefunden, soll["positionen"]):
        assert b_ist == b_soll
        assert m_ist == m_soll
        assert e_ist == pytest.approx(e_soll, abs=0.005)


@pytest.mark.parametrize("name", SOLL)
def test_summe_der_positionen_ist_netto(name):
    ist = lade(name)
    summe = sum(p["betrag"] for p in ist["positionen"])
    assert summe == pytest.approx(ist["betrag_netto"], abs=0.005)
