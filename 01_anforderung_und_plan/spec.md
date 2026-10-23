# Anforderung

## Ziel
parse_betrag(text: str) -> Decimal liest einzelne Euro-
Beträge aus Formular, CSV und
Rechnungsangaben. Es verarbeitet den Betragstext, nicht eine vollständige E-Mail oder CSV-
Zeile.

## Akzeptanzkriterien
-
A1: Given "12,50", When parse_betrag aufgerufen wird, Then Decimal("12.50").
-
A2: Given "€ 8,90", When parse_betrag aufgerufen wird, Then Decimal("8.90").
-
A3: Given "89,90 €", When parse_betrag aufgerufen wird, Then Decimal("89.90").
-
A4: Given "-1.234,00", When parse_betrag aufgerufen wird, Then Decimal("-1234.00").
-
A5: Given "12,-", When parse_betrag aufgerufen wird, Then Decimal("12").
6
-
: Given "250", When parse_betrag aufgerufen wird, Then Decimal("250").
-
A7: Given " 12,50 ", When parse_betrag aufgerufen wird, Then Decimal("12.50").
- F1: Given "212.50" oder "EUR 212.50", When parse_betrag aufgerufen wird, Then ValueError;
Punkt als Dezimaltrenner ist nicht zulässig.
- F2: Given einen leeren Text, When parse_betrag aufgerufen wird, Then ValueError.
- F3: Given "NaN" oder "Infinity", When parse_betrag aufgerufen wird, Then ValueError.

## Grenzfälle
Negative Beträge sind erlaubt. Ein Punkt ist ein Tausendertrenner, kein Dezimaltrenner.
Mehrdeutige oder noch nicht entschiedene Fälle als Rückfrage melden.

## Fehlerverhalten
Bei abgelehnten Eingaben ValueError; die Meldung nennt die beanstandete Eingabe.