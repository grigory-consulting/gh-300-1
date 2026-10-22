from datetime import datetime

from raumplan.buchung import ZEITFORMAT, Buchung
from raumplan.konflikte import finde_konflikte, ueberschneiden_sich


def buchung(raum: str, beginn: str, ende: str, von: str = "Test") -> Buchung:
    return Buchung(
        raum=raum,
        beginn=datetime.strptime(beginn, ZEITFORMAT),
        ende=datetime.strptime(ende, ZEITFORMAT),
        gebucht_von=von,
    )


def test_teilweise_ueberschneidung_ist_konflikt():
    a = buchung("1.05", "2026-10-14 09:00", "2026-10-14 10:30")
    b = buchung("1.05", "2026-10-14 10:00", "2026-10-14 11:00")
    assert ueberschneiden_sich(a, b)
    assert ueberschneiden_sich(b, a)


def test_enthaltene_buchung_ist_konflikt():
    lang = buchung("1.05", "2026-10-14 08:00", "2026-10-14 12:00")
    kurz = buchung("1.05", "2026-10-14 09:00", "2026-10-14 10:00")
    assert ueberschneiden_sich(lang, kurz)
    assert ueberschneiden_sich(kurz, lang)


def test_verschiedene_raeume_sind_kein_konflikt():
    a = buchung("1.05", "2026-10-14 09:00", "2026-10-14 10:30")
    b = buchung("2.14", "2026-10-14 09:00", "2026-10-14 10:30")
    assert not ueberschneiden_sich(a, b)


def test_buchungen_mit_pause_sind_kein_konflikt():
    a = buchung("3.01", "2026-10-14 13:00", "2026-10-14 14:00")
    b = buchung("3.01", "2026-10-14 15:00", "2026-10-14 16:00")
    assert not ueberschneiden_sich(a, b)
    assert not ueberschneiden_sich(b, a)


def test_konflikt_ueber_tagesgrenze():
    nacht = buchung("G-02", "2026-10-14 22:00", "2026-10-15 02:00")
    frueh = buchung("G-02", "2026-10-15 01:00", "2026-10-15 03:00")
    assert ueberschneiden_sich(nacht, frueh)


def test_finde_konflikte_liefert_paare_nach_beginn():
    spaet = buchung("1.05", "2026-10-14 10:00", "2026-10-14 11:00", "Schulung")
    frueh = buchung("1.05", "2026-10-14 09:00", "2026-10-14 10:30", "Personal")
    anderer_raum = buchung("2.14", "2026-10-14 09:00", "2026-10-14 10:00", "Einkauf")
    assert finde_konflikte([spaet, anderer_raum, frueh]) == [(frueh, spaet)]


def test_finde_konflikte_ohne_buchungen():
    assert finde_konflikte([]) == []
