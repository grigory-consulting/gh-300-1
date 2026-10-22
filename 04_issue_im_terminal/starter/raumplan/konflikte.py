"""Doppelbelegungen von Räumen finden."""

from __future__ import annotations

from itertools import combinations

from .buchung import Buchung


def ueberschneiden_sich(a: Buchung, b: Buchung) -> bool:
    """True, wenn a und b denselben Raum zur selben Zeit belegen."""
    if a.raum != b.raum:
        return False
    return a.beginn <= b.ende and b.beginn <= a.ende


def finde_konflikte(buchungen: list[Buchung]) -> list[tuple[Buchung, Buchung]]:
    """Alle Paare sich überschneidender Buchungen, sortiert nach Raum und Beginn."""
    sortiert = sorted(buchungen, key=lambda b: (b.raum, b.beginn))
    return [(a, b) for a, b in combinations(sortiert, 2) if ueberschneiden_sich(a, b)]
