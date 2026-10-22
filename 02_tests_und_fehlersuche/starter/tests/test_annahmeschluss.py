from datetime import date, datetime

from versand.lieferdatum import versanddatum

MITTWOCH = (2026, 10, 14)
FREITAG = (2026, 10, 16)


def test_mittwoch_morgens():
    assert versanddatum(datetime(*MITTWOCH, 9, 0)) == date(2026, 10, 14)


def test_mittwoch_13_59():
    assert versanddatum(datetime(*MITTWOCH, 13, 59)) == date(2026, 10, 14)


def test_mittwoch_14_00():
    assert versanddatum(datetime(*MITTWOCH, 14, 0)) == date(2026, 10, 15)


def test_mittwoch_14_30():
    assert versanddatum(datetime(*MITTWOCH, 14, 30)) == date(2026, 10, 15)


def test_mittwoch_15_00():
    assert versanddatum(datetime(*MITTWOCH, 15, 0)) == date(2026, 10, 15)


def test_freitag_14_20():
    assert versanddatum(datetime(*FREITAG, 14, 20)) == date(2026, 10, 19)


def test_freitag_16_00():
    assert versanddatum(datetime(*FREITAG, 16, 0)) == date(2026, 10, 19)
