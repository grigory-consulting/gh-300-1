"""Bundesweite gesetzliche Feiertage.

Gepflegt für 2026 und 2027. Regionale Feiertage sind nicht enthalten.
"""

from datetime import date

FEIERTAGE = frozenset({
    # 2026
    date(2026, 1, 1),    # Neujahr
    date(2026, 4, 3),    # Karfreitag
    date(2026, 4, 6),    # Ostermontag
    date(2026, 5, 1),    # Tag der Arbeit
    date(2026, 5, 14),   # Christi Himmelfahrt
    date(2026, 5, 25),   # Pfingstmontag
    date(2026, 10, 3),   # Tag der Deutschen Einheit
    date(2026, 12, 25),  # 1. Weihnachtstag
    date(2026, 12, 26),  # 2. Weihnachtstag
    # 2027
    date(2027, 1, 1),
    date(2027, 3, 26),
    date(2027, 3, 29),
    date(2027, 5, 1),
    date(2027, 5, 6),
    date(2027, 5, 17),
    date(2027, 10, 3),
    date(2027, 12, 25),
    date(2027, 12, 26),
})

GEPFLEGTE_JAHRE = frozenset(tag.year for tag in FEIERTAGE)


def ist_feiertag(tag: date) -> bool:
    """Prüft, ob `tag` ein bundesweiter Feiertag ist.

    Für Jahre ohne gepflegte Liste gibt es keine verlässliche Antwort,
    deshalb wird dann ValueError ausgelöst.
    """
    if tag.year not in GEPFLEGTE_JAHRE:
        raise ValueError(f"Keine Feiertage für {tag.year} hinterlegt")
    return tag in FEIERTAGE
