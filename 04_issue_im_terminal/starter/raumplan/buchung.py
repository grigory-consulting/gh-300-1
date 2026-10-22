"""Buchungen aus dem CSV-Export des Buchungsformulars lesen."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ZEITFORMAT = "%Y-%m-%d %H:%M"


@dataclass(frozen=True)
class Buchung:
    raum: str
    beginn: datetime
    ende: datetime
    gebucht_von: str

    def __post_init__(self) -> None:
        if self.ende <= self.beginn:
            raise ValueError(
                f"Buchung für Raum {self.raum}: Ende {self.ende:%d.%m.%Y %H:%M} "
                f"liegt nicht nach Beginn {self.beginn:%d.%m.%Y %H:%M}"
            )


def lies_buchungen(pfad: str | Path) -> list[Buchung]:
    """Liest eine CSV-Datei mit den Spalten raum;beginn;ende;gebucht_von."""
    buchungen = []
    with open(pfad, encoding="utf-8", newline="") as datei:
        for zeile in csv.DictReader(datei, delimiter=";"):
            buchungen.append(
                Buchung(
                    raum=zeile["raum"].strip(),
                    beginn=datetime.strptime(zeile["beginn"].strip(), ZEITFORMAT),
                    ende=datetime.strptime(zeile["ende"].strip(), ZEITFORMAT),
                    gebucht_von=zeile["gebucht_von"].strip(),
                )
            )
    return buchungen
