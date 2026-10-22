# Übung 2: Nach dem eigenen Versuch

Lesen Sie jeden Abschnitt erst, wenn Sie den zugehörigen Teil selbst bearbeitet haben. Das README sagt Ihnen, wann.

## 1. Teil A

### Debug-Prompt (Schritte 3 und 4), im Agenten **Ask**

> **Problem:** `test_bestellung_ostermontag_vormittag` in `tests/test_lieferdatum.py` schlägt fehl.
>
> **Erwartet:** Eine Bestellung am Ostermontag, 06.04.2026, 09:30 Uhr verlässt das Lager laut `#file:docs/fachregeln.md` am Dienstag, 07.04.2026. Ostermontag ist ein Feiertag und damit kein Versandtag.
>
> **Tatsächlich:** `versanddatum` liefert den 06.04.2026.
>
> **Reproduktion:** `python -m pytest tests/test_lieferdatum.py -k ostermontag`
>
> **Relevanter Code:** `#file:versand/lieferdatum.py`, Testausgabe:
> ```
> (Ausgabe hier einfügen)
> ```
>
> **Bisher geprüft:** Der 06.04.2026 ist ein Montag und laut Fachregeln Abschnitt 1 ein Feiertag. Der Test erwartet also zu Recht den Dienstag.
>
> **Auftrag:** Nenne bis zu drei Hypothesen für die Ursache, nach Wahrscheinlichkeit geordnet. Gib zu jeder Hypothese eine Prüfung an, die sie widerlegen würde, und was ich dabei sehen müsste. Ändere keinen Code und schlage noch keinen Fix vor.

### Zwei Prüfungen (Schritt 5)

Erkennt `ist_feiertag` den Ostermontag?

```bash
python -c "from datetime import date; from versand.feiertage import ist_feiertag; print(ist_feiertag(date(2026, 4, 6)))"
```

Und mit dem Wert, den `versanddatum` tatsächlich weitergibt?

```bash
python -c "from datetime import datetime; from versand.feiertage import ist_feiertag; print(ist_feiertag(datetime(2026, 4, 6, 9, 30)))"
```

Erst der Unterschied zwischen beiden Ausgaben zeigt die Ursache.

### Fix-Prompt (Schritt 6), im Agenten **Agent**

> Hypothese 1 ist bestätigt: (in einem Satz, was Sie geprüft und gesehen haben). Behebe nur diese Ursache in `versand/lieferdatum.py`, so klein wie möglich. Keine weiteren Änderungen, kein Umbau. Zeige mir den Diff und lass danach `python -m pytest tests/test_lieferdatum.py` laufen.

### Die beiden übrigen Fehlschläge (Schritt 7), im Agenten **Agent**

> Laut `docs/fachregeln.md`, Abschnitt 1, sind Zustelltage Montag bis Samstag ohne Feiertage. `zustelltermin` in `versand/lieferdatum.py` zählt stattdessen Versandtage, also Montag bis Freitag. Behebe nur diese Ursache, so klein wie möglich, und lass danach `python -m pytest tests/test_lieferdatum.py` laufen.

## 2. Teil B

Ein kurzer Auftrag, im Agenten **Agent**:

> Lass `python -m pytest` laufen und behebe die Fehlschläge. Prüfe danach mit einem zweiten Testlauf, dass alles grün ist.

## 3. Teil C

### Liste (Schritt 2), im Agenten **Ask**

> `#file:versand/lieferdatum.py` `#file:versand/feiertage.py` `#file:versand/konfiguration.py` `#file:docs/fachregeln.md` und die Tests in `tests/`.
>
> Welche Grenzfälle aus den Fachregeln sind durch die vorhandenen Tests nicht abgedeckt? Liste jeden Fall mit einer Bestellung als Beispiel (Datum, Uhrzeit, Versandart), dem laut Fachregeln erwarteten Ergebnis und einer Begründung, warum der Fall fachlich wichtig ist. Schreibe noch keine Tests.

### Umsetzung (Schritt 4), im Agenten **Agent**

> Setze die Fälle 2, 4 und 5 aus deiner Liste als pytest-Tests in einer neuen Datei `tests/test_grenzfaelle.py` um, im Stil der vorhandenen Tests. Leite die erwarteten Werte aus `docs/fachregeln.md` ab, nicht aus dem Code. Ändere keine anderen Dateien. Lass danach `python -m pytest` laufen.

## 4. Reflexion

Erst lesen, wenn Sie mit Teil C fertig sind.

**Teil A**

- Welche Hypothese hat Copilot als wahrscheinlichste genannt? Hat sie Ihrer Prüfung standgehalten?
- Welche Prüfung hat die Ursache sichtbar gemacht?
- Hat ein Fix mehr geändert als die bestätigte Ursache?

**Teil B**

Suchen Sie Ihren Commit aus Teil B heraus:

```bash
git log --stat -- .
```

- Welche Dateien hat der Commit geändert?
- Was war falsch: das, was der Agent geändert hat, oder das, was er stehen ließ? Woran erkennen Sie das?
- Welche Signale außer den Fachregeln hätte es in einem echten Projekt gegeben, zum Beispiel im `git log` der geänderten und der unveränderten Datei oder im Ticket zur Änderung?

**Teil C**

- Hat Copilot die beiden Fälle aus Ihrer Vorhersage genannt?
- Woher stammen die erwarteten Werte in den neuen Tests: aus den Fachregeln oder aus dem, was der Code gerade liefert?
