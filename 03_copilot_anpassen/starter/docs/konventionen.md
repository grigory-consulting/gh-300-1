# Wie wir im Lagerprojekt arbeiten

Notiz aus der Teambesprechung im Frühjahr, seitdem zweimal ergänzt. Wer neu dazukommt, liest das bitte einmal ganz. Ein Linter prüft davon nichts, wir achten im Review darauf.

## Wofür der Code da ist

Das Paket `lager` liest den CSV-Export unserer Lagerverwaltung und rechnet aus, was nachbestellt werden muss. Die Skripte unter `scripts/` sind die Werkzeuge, die die Kollegen an der Theke im Terminal aufrufen; dort lesen sie auch das Ergebnis. Geht etwas schief, steht die Meldung auf stderr, und das Skript endet mit Exit-Code 1.

Fehlermeldungen lesen also Menschen, die nicht programmieren, und deshalb schreiben wir sie auf Deutsch. Eine Meldung nennt den Wert, der nicht passt, und wenn es um eine Datei geht, auch Dateiname und Zeile. "Ungültige Eingabe" allein hilft an der Theke niemandem. Wir werfen die eingebauten Ausnahmen (`ValueError` für falsche Daten, `FileNotFoundError` für fehlende Dateien) und keine eigenen Ausnahmeklassen, und schon gar kein nacktes `Exception`.

## Ausgaben und Protokoll

Wir verwenden kein `print`, sondern das Modul `logging`. Jedes Modul holt sich am Anfang mit `logger = logging.getLogger(__name__)` einen eigenen Logger. Was übersprungen oder korrigiert wird, ist eine Warnung, alles andere höchstens `info`. Wie das Protokoll aussieht und wohin es geht, legen die Skripte fest; im Paket ruft niemand `logging.basicConfig` auf.

## Code

Wir arbeiten mit Python 3.12 und nur mit der Standardbibliothek. Für die Tests nehmen wir pytest, sonst kommt nichts dazu. Wer meint, eine Bibliothek zu brauchen, fragt vorher im Team.

Jede Funktion im Paket und in den Skripten bekommt Typannotationen, auch für den Rückgabewert, und zwar in der heutigen Schreibweise: `list[Artikel]` und `str | None`, nicht `List` oder `Optional` aus `typing`. Öffentliche Funktionen haben einen Docstring, der in einem Satz sagt, was herauskommt.

Pfade sind `pathlib.Path`, als Parameter wie im Inneren der Funktion. `os.path` verwenden wir nicht mehr. Dateien öffnen wir mit `with`. CSV-Dateien schreiben und lesen wir mit dem Modul `csv`, Trennzeichen Semikolon (sonst öffnet die Buchhaltung sie in Excel falsch), Kodierung UTF-8, mit Kopfzeile und `newline=""` beim Öffnen.

## Tests

Tests liegen unter `tests/` und sind schlichte pytest-Funktionen. Neue Testklassen mit `setUp` schreiben wir nicht mehr. Was mehrere Tests brauchen, wird eine Fixture in `tests/conftest.py`. Bevor Sie eine neue anlegen, sehen Sie dort nach, ob es die passende schon gibt. Dateien legen Tests nur in `tmp_path` an, nie im Projektordner. Der Testname sagt auf Deutsch, welches Verhalten geprüft wird, etwa `test_zeile_ohne_nummer_wird_mit_warnung_uebersprungen`. Bei Fehlerfällen prüfen wir mit `pytest.raises(..., match=...)` auch den Text der Meldung, weil der für uns zum Verhalten gehört.

## Alter Code

`lager/export.py` und `tests/test_auswertung.py` stammen aus der ersten Version und halten sich noch nicht an diese Regeln. Wir bauen sie nicht in einem Rutsch um. Wer dort etwas ändert oder ergänzt, schreibt den neuen oder geänderten Teil nach den Regeln und lässt den Rest der Datei, wie er ist. Aufräumen machen wir in eigenen Commits, nicht nebenbei.

## Befehle

Tests laufen im Projektordner mit `python -m pytest`. Den Bericht startet man mit `python -m scripts.bestandsbericht daten/bestand.csv`.
