"""Aufruf: python -m raumplan pruefen DATEI.csv

Gibt jede Doppelbelegung aus. Exit-Code 0 ohne Konflikte, 1 mit Konflikten.
"""

from __future__ import annotations

import argparse
import sys

from .buchung import Buchung, lies_buchungen
from .konflikte import finde_konflikte


def _zeitraum(b: Buchung) -> str:
    if b.beginn.date() == b.ende.date():
        return f"{b.beginn:%d.%m.%Y %H:%M}-{b.ende:%H:%M}"
    return f"{b.beginn:%d.%m.%Y %H:%M}-{b.ende:%d.%m.%Y %H:%M}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="raumplan")
    befehle = parser.add_subparsers(dest="befehl", required=True)
    pruefen = befehle.add_parser("pruefen", help="Buchungsdatei auf Doppelbelegungen prüfen")
    pruefen.add_argument("datei")
    args = parser.parse_args(argv)

    konflikte = finde_konflikte(lies_buchungen(args.datei))
    for a, b in konflikte:
        print(
            f"Konflikt in Raum {a.raum}: {_zeitraum(a)} ({a.gebucht_von}) "
            f"und {_zeitraum(b)} ({b.gebucht_von})"
        )
    if not konflikte:
        print("Keine Konflikte gefunden.")
        return 0
    anzahl = len(konflikte)
    print(f"{anzahl} {'Konflikt' if anzahl == 1 else 'Konflikte'} gefunden.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
