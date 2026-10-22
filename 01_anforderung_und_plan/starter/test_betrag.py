from decimal import Decimal

from betrag import parse_betrag


def test_betrag_mit_komma():
    assert parse_betrag("12,50") == Decimal("12.50")


def test_betrag_mit_eurozeichen():
    assert parse_betrag("1.234,56 €") == Decimal("1234.56")


def test_kleiner_betrag():
    assert parse_betrag("0,99 €") == Decimal("0.99")


def test_ganzer_betrag():
    assert parse_betrag("250") == Decimal("250")


def test_ergebnis_ist_decimal():
    assert isinstance(parse_betrag("12,50"), Decimal)
