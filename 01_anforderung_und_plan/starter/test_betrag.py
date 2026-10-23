from decimal import Decimal

import pytest

from betrag import parse_betrag


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("12,50", "12.50"),
        ("€ 8,90", "8.90"),
        ("89,90 €", "89.90"),
        ("-1.234,00", "-1234.00"),
        ("12,-", "12"),
        ("250", "250"),
        (" 12,50 ", "12.50"),
        ("1.234,56 €", "1234.56"),
        ("0,99 €", "0.99"),
        ("1 234,56", "1234.56"),
        ("EUR 12,50", "12.50"),
        ("12,50 EUR", "12.50"),
        ("12,5", "12.5"),
        ("12,500", "12.500"),
        ("1.234.567,89", "1234567.89"),
    ],
)
def test_parse_betrag_akzeptierte_formate(text, expected):
    assert parse_betrag(text) == Decimal(expected)


@pytest.mark.parametrize(
    "text",
    [
        "212.50",
        "EUR 212.50",
        "",
        "   ",
        "NaN",
        "Infinity",
        "-Infinity",
        "1.23,45",
        "1.2345,00",
        "1 23,00",
        "1.234 567,00",
        "€ 12,50 EUR",
    ],
)
def test_parse_betrag_lehnt_ungueltige_formate_ab(text):
    with pytest.raises(ValueError) as error:
        parse_betrag(text)

    assert repr(text) in str(error.value)


def test_ergebnis_ist_decimal():
    assert isinstance(parse_betrag("12,50"), Decimal)
