"""Bestandsliste aus dem CSV-Export der Lagerverwaltung lesen."""

import csv
import logging
from pathlib import Path

from lager.artikel import Artikel

logger = logging.getLogger(__name__)

SPALTEN = ("nummer", "bezeichnung", "lagerort", "bestand", "mindestbestand", "sollbestand")


def _menge(text: str | None, spalte: str, pfad: Path, zeile: int) -> int:
    """Liest eine Stückzahl und meldet ungültige Werte mit Datei und Zeile."""
    wert_text = (text or "").strip()
    try:
        wert = int(wert_text)
    except ValueError:
        raise ValueError(
            f"{pfad.name}, Zeile {zeile}: '{wert_text}' in Spalte {spalte} ist keine ganze Zahl"
        ) from None
    if wert < 0:
        raise ValueError(f"{pfad.name}, Zeile {zeile}: {spalte} darf nicht negativ sein, gefunden {wert}")
    return wert


def lade_bestand(pfad: Path) -> list[Artikel]:
    """Liest alle Artikel aus einer Bestandsdatei (Semikolon, UTF-8, mit Kopfzeile).

    Zeilen ohne Artikelnummer werden mit einer Warnung übersprungen.
    """
    if not pfad.is_file():
        raise FileNotFoundError(f"Bestandsdatei nicht gefunden: {pfad}")

    artikel: list[Artikel] = []
    with pfad.open(encoding="utf-8", newline="") as datei:
        leser = csv.DictReader(datei, delimiter=";")
        fehlend = set(SPALTEN) - set(leser.fieldnames or [])
        if fehlend:
            raise ValueError(f"{pfad.name}: Spalten fehlen: {', '.join(sorted(fehlend))}")

        for zeile, eintrag in enumerate(leser, start=2):
            nummer = (eintrag["nummer"] or "").strip()
            if not nummer:
                logger.warning("%s, Zeile %d: keine Artikelnummer, Zeile übersprungen", pfad.name, zeile)
                continue
            mindestbestand = _menge(eintrag["mindestbestand"], "mindestbestand", pfad, zeile)
            sollbestand = _menge(eintrag["sollbestand"], "sollbestand", pfad, zeile)
            if sollbestand < mindestbestand:
                raise ValueError(
                    f"{pfad.name}, Zeile {zeile}: Sollbestand {sollbestand} liegt unter "
                    f"Mindestbestand {mindestbestand}"
                )
            artikel.append(
                Artikel(
                    nummer=nummer,
                    bezeichnung=(eintrag["bezeichnung"] or "").strip(),
                    lagerort=(eintrag["lagerort"] or "").strip(),
                    bestand=_menge(eintrag["bestand"], "bestand", pfad, zeile),
                    mindestbestand=mindestbestand,
                    sollbestand=sollbestand,
                )
            )

    logger.info("%d Artikel aus %s gelesen", len(artikel), pfad.name)
    return artikel
