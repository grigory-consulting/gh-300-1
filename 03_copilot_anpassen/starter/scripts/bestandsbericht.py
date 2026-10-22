"""Zeigt alle Artikel unter Mindestbestand mit der Bestellmenge an.

Aufruf im Projektordner:

    python -m scripts.bestandsbericht daten/bestand.csv
"""

import argparse
import logging
import sys
from pathlib import Path

from lager.auswertung import bestellmenge, unter_mindestbestand
from lager.einlesen import lade_bestand


def main(argv: list[str] | None = None) -> int:
    """Gibt den Bericht auf stdout aus und liefert den Exit-Code."""
    parser = argparse.ArgumentParser(description="Artikel unter Mindestbestand anzeigen")
    parser.add_argument("bestandsdatei", type=Path, help="CSV-Export der Lagerverwaltung")
    parser.add_argument("--ausfuehrlich", action="store_true", help="Protokollmeldungen anzeigen")
    argumente = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if argumente.ausfuehrlich else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )

    try:
        artikel = lade_bestand(argumente.bestandsdatei)
    except (FileNotFoundError, ValueError) as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return 1

    knapp = unter_mindestbestand(artikel)
    if not knapp:
        print("Alle Artikel über Mindestbestand.")
        return 0

    print(f"{len(knapp)} Artikel unter Mindestbestand:")
    for a in knapp:
        print(f"  {a.lagerort:<6} {a.nummer:<10} {a.bezeichnung:<32} Bestand {a.bestand:>3}  bestellen {bestellmenge(a):>3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
