"""Geldbeträge aus Texteingaben lesen."""

from decimal import Decimal


def parse_betrag(text: str) -> Decimal:
    """Liest einen Betrag wie "1.234,56 €" und gibt ihn als Decimal zurück."""
    zahl = text.replace("€", "").strip()
    zahl = zahl.replace(".", "").replace(",", ".")
    return Decimal(zahl)
