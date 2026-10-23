"""Geldbeträge aus Texteingaben lesen."""

import re
from decimal import Decimal


_BETRAG_PATTERN = re.compile(
    r"-?(?:[0-9]+|[0-9]{1,3}(?:\.[0-9]{3})+|[0-9]{1,3}(?: [0-9]{3})+)"
    r"(?:,[0-9]+|,-)?"
)


def parse_betrag(text: str) -> Decimal:
    """Liest einen deutschen Euro-Betrag und gibt ihn als Decimal zurück."""
    zahl = text.strip()
    waehrung_vorne = zahl.startswith(("€", "EUR"))
    if waehrung_vorne:
        waehrung = "€" if zahl.startswith("€") else "EUR"
        zahl = zahl[len(waehrung) :].strip()

    waehrung_hinten = zahl.endswith(("€", "EUR"))
    if waehrung_hinten:
        if waehrung_vorne:
            raise ValueError(f"Ungültiger Betrag: {text!r}")
        waehrung = "€" if zahl.endswith("€") else "EUR"
        zahl = zahl[: -len(waehrung)].strip()

    if not _BETRAG_PATTERN.fullmatch(zahl):
        raise ValueError(f"Ungültiger Betrag: {text!r}")

    normalisiert = zahl.replace(".", "").replace(" ", "").replace(",-", "")
    normalisiert = normalisiert.replace(",", ".")
    betrag = Decimal(normalisiert)
    if not betrag.is_finite():
        raise ValueError(f"Ungültiger Betrag: {text!r}")
    return betrag
