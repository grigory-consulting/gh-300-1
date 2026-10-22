from datetime import date

from versand.feiertage import ist_feiertag


def test_pfingstmontag_2027():
    assert ist_feiertag(date(2027, 5, 17))


def test_heiligabend_ist_kein_feiertag():
    assert not ist_feiertag(date(2026, 12, 24))


def test_gewoehnlicher_sonntag():
    assert not ist_feiertag(date(2026, 10, 18))
