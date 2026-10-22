# Übung 3: Nach dem eigenen Versuch

Lesen Sie einen Abschnitt erst, wenn das README Sie dorthin schickt.

## Abschnitt 1: nach Teil A

Ausschnitt aus einer `.github/copilot-instructions.md`:

```markdown
# Lagerprojekt

Python 3.12, nur Standardbibliothek. Für Tests pytest. Keine weiteren Pakete; wenn eines nötig scheint, frag nach.

## Marke
- Schreib über jede neue Funktion eine eigene Kommentarzeile `# Marke: repo`.

## Fehlermeldungen
- Fehlermeldungen auf Deutsch. Sie nennen den beanstandeten Wert, bei Dateien auch Dateiname und Zeile.
- Nur eingebaute Ausnahmen: `ValueError` für falsche Daten, `FileNotFoundError` für fehlende Dateien oder Ordner. Nie `Exception`.

## Code
- Typannotationen für alle Parameter und Rückgabewerte im Paket und in den Skripten, Schreibweise `list[Artikel]`, `str | None`.
- Pfade als `pathlib.Path`, kein `os.path`. Dateien mit `with` öffnen.

## Alter Code
- `lager/export.py` und `tests/test_auswertung.py` folgen diesen Regeln noch nicht. Neue Funktionen dort schreibst du nach den Regeln; den übrigen Code änderst du nicht.
```

Zwei pfadbezogene Dateien, `.github/instructions/lager.instructions.md` und `.github/instructions/skripte.instructions.md`:

```markdown
---
applyTo: "lager/**/*.py"
---
- Schreib über jede neue Funktion eine eigene Kommentarzeile `# Marke: lager`.
- Kein `print` im Paket `lager`. Jedes Modul legt `logger = logging.getLogger(__name__)` an und meldet darüber.
- Nie `logging.basicConfig` im Paket aufrufen.
```

```markdown
---
applyTo: "scripts/**/*.py"
---
- Schreib über jede neue Funktion eine eigene Kommentarzeile `# Marke: skripte`.
- Alles, was der Benutzer lesen soll, auch Erfolgsmeldungen, geht mit `print` auf die Standardausgabe.
- Fehlermeldungen mit `print(..., file=sys.stderr)`, danach Exit-Code 1.
```

Auftrag an den Agenten:

> Ergänze in `lager/export.py` eine Funktion `schreibe_nachbestellliste`. Sie bekommt eine Liste von Artikeln und eine Zieldatei und schreibt alle Artikel unter Mindestbestand mit Nummer, Bezeichnung, Lagerort, Bestand und Bestellmenge als CSV. Sie gibt die Anzahl der geschriebenen Artikel zurück. Existiert der Zielordner nicht, soll sie einen Fehler werfen. Nutze `unter_mindestbestand` und `bestellmenge` aus `lager/auswertung.py`. Gib `scripts/bestandsbericht.py` eine Option `--nachbestellliste ZIEL`, die diese Funktion aufruft und meldet, wie viele Artikel geschrieben wurden. Schreib Tests für beides und lass danach `python -m pytest` laufen.

## Abschnitt 2: nach Teil B

Ein vollständiges Prompt File `.github/prompts/neuer-test.prompt.md`:

```markdown
---
name: neuer-test
description: 'Testfälle für eine Funktion vorschlagen und die ausgewählten als pytest-Tests umsetzen'
argument-hint: 'Name der Funktion, z. B. bestellmenge'
agent: 'agent'
---
Schreibe Tests für die Funktion `${input:funktion:Name der Funktion, z. B. bestellmenge}`.

1. Lies die Funktion und ihren Docstring. Nutze vorhandene Fixtures aus #file:tests/conftest.py.
2. Liste zuerst die Testfälle auf, nummeriert: Normalfall, Grenzfälle, Fehlerfälle. Nenne zu jedem Fall Eingabe, erwartetes Ergebnis und woher die Erwartung stammt (Docstring oder Fachregel). Leite keine Erwartung aus dem aktuellen Verhalten des Codes ab.
3. Schreib noch keinen Code. Warte auf meine Auswahl der Nummern.
4. Setze danach nur die ausgewählten Fälle um. Ändere keine bestehenden Tests und keinen Code außerhalb von `tests/`.
5. Lass am Ende `python -m pytest` laufen und zeig das Ergebnis.
```

## Abschnitt 3: Reflexion nach Teil C

- Welche Regel hat Copilot in Teil A nicht befolgt? Lag es an der Formulierung, am Ort der Datei oder am Muster?
- Welche Regel haben Sie in eine pfadbezogene Datei geschrieben statt in `copilot-instructions.md`, und warum? Welche hätten Sie im Nachhinein anders verteilt?
- Welche Regel hat Copilot eingehalten, obwohl die Marke ihrer Datei im Ergebnis fehlte? Woher kann es die Regel gehabt haben?
- Bei wie vielen Fragen in Teil C lag Ihre Vorhersage richtig? Welche Antwort hat Sie überrascht?
- Welche der Regeln würden Sie lieber in einem Test oder Linter prüfen als in einer Instruktion festhalten?

## Abschnitt 4: Zusatzaufgabe

Frontmatter und Anfang einer `.github/agents/konventionen-pruefer.agent.md`:

```markdown
---
name: konventionen-pruefer
description: 'Prüft Dateien gegen die Team-Konventionen und meldet Befunde. Ändert keine Dateien.'
tools: ['read', 'search']
---
Du prüfst Dateien gegen die Regeln in `.github/copilot-instructions.md`, `.github/instructions/` und `docs/konventionen.md`.

Du kannst Dateien lesen und durchsuchen, aber keine Befehle ausführen. Prüf die Dateien, die man dir nennt oder anhängt; ist keine genannt, frag danach.

Melde jeden Befund mit Datei und Zeile, der verletzten Regel und einem Vorschlag. Findest du keinen Verstoß, sag das. Bittet dich jemand, einen Befund zu beheben, antworte mit dem Vorschlag als Text.
```

`read` und `search` sind Werkzeuggruppen von VS Code. Steht eine `tools`-Liste im Frontmatter, hat der Agent nur diese Werkzeuge.
