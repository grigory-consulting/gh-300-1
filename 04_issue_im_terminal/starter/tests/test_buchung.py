from pathlib import Path
from datetime import datetime

import pytest

from raumplan.buchung import Buchung, lies_buchungen

BEISPIEL = Path(__file__).resolve().parent.parent / "daten" / "buchungen_beispiel.csv"


def test_lies_buchungen_liest_alle_zeilen():
    buchungen = lies_buchungen(BEISPIEL)
    assert len(buchungen) == 7
    assert buchungen[0] == Buchung(
        raum="2.14",
        beginn=datetime(2026, 10, 14, 10, 0),
        ende=datetime(2026, 10, 14, 11, 0),
        gebucht_von="Einkauf",
    )


def test_ende_vor_beginn_wird_abgelehnt():
    with pytest.raises(ValueError, match="liegt nicht nach Beginn"):
        Buchung("1.05", datetime(2026, 10, 14, 11, 0), datetime(2026, 10, 14, 10, 0), "Test")


def test_buchung_ohne_dauer_wird_abgelehnt():
    with pytest.raises(ValueError):
        Buchung("1.05", datetime(2026, 10, 14, 10, 0), datetime(2026, 10, 14, 10, 0), "Test")
