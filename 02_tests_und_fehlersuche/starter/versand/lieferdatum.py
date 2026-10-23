"""Versandtag und Zustelltermin einer Bestellung."""

from datetime import date, datetime, timedelta

from versand.feiertage import ist_feiertag
from versand.konfiguration import ANNAHMESCHLUSS, ZUSTELLTAGE

EIN_TAG = timedelta(days=1)


def ist_versandtag(tag: date) -> bool:
    """Montag bis Freitag, sofern kein Feiertag."""
    return tag.weekday() < 5 and not ist_feiertag(tag)


def ist_zustelltag(tag: date) -> bool:
    """Montag bis Samstag, sofern kein Feiertag."""
    return tag.weekday() < 6 and not ist_feiertag(tag)


def naechster_versandtag(tag: date) -> date:
    """Erster Versandtag nach `tag`."""
    tag += EIN_TAG
    while not ist_versandtag(tag):
        tag += EIN_TAG
    return tag


def versanddatum(bestellt: datetime) -> date:
    """Tag, an dem die Bestellung das Lager verlässt."""
    if ist_versandtag(bestellt) and bestellt.time() < ANNAHMESCHLUSS:
        return bestellt.date()
    return naechster_versandtag(bestellt.date())


def zustelltermin(bestellt: datetime, versandart: str = "standard") -> date:
    """Tag, an dem das Paket beim Kunden ankommt."""
    if versandart not in ZUSTELLTAGE:
        raise ValueError(f"Unbekannte Versandart: {versandart!r}")

    tag = versanddatum(bestellt)
    offen = ZUSTELLTAGE[versandart]
    while offen > 0:
        tag += EIN_TAG
        if ist_zustelltag(tag):
            offen -= 1
    return tag
