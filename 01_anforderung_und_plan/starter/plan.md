# Plan: `parse_betrag` gemäß Spezifikation

## Problem und Ansatz

`parse_betrag` entfernt derzeit pauschal Punkte und ersetzt Kommas, sodass ungültige Formate wie `212.50` falsch interpretiert werden können. Der Parser soll stattdessen deutsche Euro-Beträge nach einer klaren Eingabegrammatik validieren und nur dann in `Decimal` umwandeln.

## Umfang und Entscheidungen

- Die ausdrücklich genannten Beispiele bleiben unterstützt: Komma-Dezimaltrenner, optionale `€`-Kennzeichnung am Anfang oder Ende, negatives Vorzeichen, ganzzahlige Beträge, `12,-` und äußere Leerzeichen.
- Zusätzlich werden Tausendergruppen mit Leerzeichen, der Währungscode `EUR` bei Kommaformat sowie variable Nachkommastellen akzeptiert.
- Punkte sind ausschließlich Tausendertrenner und müssen in gültigen Dreiergruppen stehen; Punkt-Dezimalformate wie `212.50` werden mit `ValueError` abgelehnt.
- Leere Eingaben, `NaN`, `Infinity` und sonstige ungültige oder mehrdeutige Schreibweisen werden mit `ValueError` abgelehnt. Die Fehlermeldung nennt die ursprüngliche Eingabe.
- Es wird nur der einzelne Betragstext verarbeitet, keine komplette CSV-Zeile oder E-Mail.

## Umsetzung

1. Tests für alle spezifizierten Beispiele, zusätzlich erlaubte Varianten und Fehlerfälle ergänzen.
2. `parse_betrag` um Formatvalidierung und sichere `Decimal`-Konvertierung erweitern.
3. Gezielte Tests ausführen und sicherstellen, dass erwartete Werte sowie `ValueError`-Fehler einschließlich Eingabe in der Meldung geprüft werden.
