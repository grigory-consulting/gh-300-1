from datetime import date, datetime

from versand.lieferdatum import versanddatum, zustelltermin


def test_bestellung_dienstag_vormittag_standard():
    bestellt = datetime(2026, 10, 13, 10, 15)
    assert versanddatum(bestellt) == date(2026, 10, 13)
    assert zustelltermin(bestellt) == date(2026, 10, 15)


def test_bestellung_dienstag_abend():
    assert versanddatum(datetime(2026, 10, 13, 18, 40)) == date(2026, 10, 14)


def test_bestellung_samstag():
    assert versanddatum(datetime(2026, 10, 17, 11, 0)) == date(2026, 10, 19)


def test_bestellung_sonntag_express():
    bestellt = datetime(2026, 10, 18, 20, 0)
    assert versanddatum(bestellt) == date(2026, 10, 19)
    assert zustelltermin(bestellt, "express") == date(2026, 10, 20)


def test_bestellung_montag_express():
    assert zustelltermin(datetime(2026, 10, 19, 8, 5), "express") == date(2026, 10, 20)


def test_bestellung_donnerstag_vormittag_standard():
    assert zustelltermin(datetime(2026, 10, 15, 9, 0)) == date(2026, 10, 17)


def test_bestellung_freitag_vormittag_express():
    assert zustelltermin(datetime(2026, 10, 16, 11, 30), "express") == date(2026, 10, 17)


def test_bestellung_am_abend_vor_himmelfahrt():
    assert versanddatum(datetime(2026, 5, 13, 19, 0)) == date(2026, 5, 15)


def test_bestellung_ostermontag_vormittag():
    assert versanddatum(datetime(2026, 4, 6, 9, 30)) == date(2026, 4, 7)
