# Übung 3: Copilot für ein Repository anpassen

**Lernziel:** Sie halten die Konventionen eines Teams in Instruktionsdateien fest, legen fest, für welchen Teil des Repos welche Regel gilt, und schreiben ein Prompt File für eine wiederkehrende Aufgabe. Dann prüfen Sie am Diff und an der Ausgabe, ob und wo Ihre Anpassungen wirken.

**Dauer:** etwa 35 Minuten

## Ausgangslage

Eine Fahrradwerkstatt führt ihr Ersatzteillager mit einem kleinen Python-Projekt. Das Paket `lager` liest den CSV-Export der Lagerverwaltung und berechnet, was nachbestellt werden muss. Ein Skript zeigt den Kollegen an der Theke die knappen Artikel an.

| Datei | Inhalt |
|---|---|
| `lager/artikel.py` | Datenmodell `Artikel` |
| `lager/einlesen.py` | `lade_bestand`: Bestandsdatei lesen und prüfen |
| `lager/auswertung.py` | `unter_mindestbestand`, `bestellmenge` |
| `lager/export.py` | Export für die Buchhaltung (alter Code) |
| `scripts/bestandsbericht.py` | Bericht im Terminal |
| `tests/` | pytest-Tests, gemeinsame Fixtures in `conftest.py` |
| `daten/bestand.csv` | Beispieldaten |
| `docs/konventionen.md` | Team-Notiz: wie im Projekt gearbeitet wird |

Das Team hat seine Regeln in [starter/docs/konventionen.md](starter/docs/konventionen.md) aufgeschrieben. Kein Werkzeug prüft sie, das Team achtet im Review darauf. Copilot kennt diese Notiz nur, wenn sie zufällig im Kontext landet. Das ändern Sie in dieser Übung.

## Vorbereitung

1. Ihre Anpassungsdateien gehören zu diesem kleinen Projekt, nicht zum ganzen Übungsrepo. Öffnen Sie deshalb den Ordner `starter` als eigenen Arbeitsbereich:

   ```bash
   cd "$(git rev-parse --show-toplevel)/03_copilot_anpassen/starter"
   code -r .
   ```

   Das Fenster lädt neu, im Explorer stehen danach nur noch `daten`, `docs`, `lager`, `scripts` und `tests`. Fragt VS Code, ob Sie den Autoren des Ordners vertrauen, bestätigen Sie. Fragt VS Code, ob es das Git-Repository aus einem übergeordneten Ordner öffnen soll, stimmen Sie ebenfalls zu, sonst bleibt die Quellcodeverwaltung leer.

   Erscheint keine Nachfrage und die Quellcodeverwaltung zeigt stattdessen einen Hinweis auf ein Repository im übergeordneten Ordner, wählen Sie dort **Open Repository** und anschließend die Wurzel des Übungsrepos.

   Klappt `code -r` nicht: **Datei > Ordner öffnen** und den Ordner `starter` wählen.

2. Öffnen Sie ein neues Terminal. Es startet jetzt im Ordner `starter`. Prüfen Sie den Ausgangsstand:

   ```bash
   git status
   python -m pytest
   ```

   Alle Tests laufen grün. `git status` soll keine offenen Änderungen zeigen. Committen Sie sonst zuerst Ihre Arbeit aus den vorigen Übungen: `git add -A && git commit -m "Übungen 1 und 2"`.

3. Stellen Sie im Chat als Harness (Session Target) **Local** ein und bleiben Sie für die ganze Übung dabei.

## Teil A: Instruktionen schreiben und ihre Wirkung prüfen

1. Lesen Sie `docs/konventionen.md`. Entscheiden Sie für jede Regel: Gilt sie im ganzen Projekt oder nur in einem Teil (`lager/`, `scripts/`, `tests/`)?

2. Schreiben Sie selbst, ohne Chat und ohne `/init` oder `/create-instructions`:

   - **`.github/copilot-instructions.md`** mit den Regeln, die überall gelten. Die Datei hat kein Frontmatter, nur Markdown.
   - **mindestens eine pfadbezogene Datei** `.github/instructions/<name>.instructions.md` für einen Teil des Projekts. Sie beginnt mit Frontmatter, das festlegt, für welche Dateien sie gilt:

     ```markdown
     ---
     applyTo: "<Muster>"
     ---
     ```

     Das Muster ist ein Glob, mehrere Muster stehen durch Komma getrennt in einem String, etwa `"**/*.ts,**/*.tsx"`.

   Schreiben Sie kurze, prüfbare Regeln, keine Abschrift der Team-Notiz. Prüfstein: Jede Regel sollte man im Diff als eingehalten oder verletzt erkennen können.

3. **Markerregel.** Copilot kann jede Regel der Team-Notiz auch aus der Notiz selbst oder aus dem vorhandenen Code übernehmen. Ob eine Instruktionsdatei gewirkt hat, sehen Sie an einer normalen Regel deshalb nicht. Ergänzen Sie in jeder Ihrer Dateien eine Regel, die sonst nirgends im Projekt steht. In `copilot-instructions.md`:

   ```markdown
   - Schreib über jede neue Funktion eine eigene Kommentarzeile `# Marke: repo`.
   ```

   In jeder pfadbezogenen Datei dieselbe Regel mit dem Namen der Datei, in `tests.instructions.md` also `# Marke: tests`. Steht eine Marke in einem Ergebnis, war die zugehörige Datei im Kontext.

4. Committen Sie diesen Stand, damit `git diff` später nur zeigt, was Copilot geändert hat:

   ```bash
   git add . && git commit -m "Instruktionen"
   ```

5. Öffnen Sie einen **neuen Chat**, wählen Sie den Agenten **Agent** und lassen Sie diese Erweiterung bauen:

   > In `lager/export.py` kommt eine Funktion dazu, die eine Nachbestellliste als CSV-Datei schreibt: alle Artikel unter Mindestbestand mit ihrer Bestellmenge. Der Aufrufer gibt die Zieldatei an, die Funktion liefert die Anzahl der geschriebenen Artikel. Existiert der Zielordner nicht, ist das ein Fehler. Der Bericht `scripts/bestandsbericht.py` bekommt eine Option `--nachbestellliste ZIEL`, die diese Liste schreibt und meldet, wie viele Artikel darin stehen. Dazu gehören Tests.

   Formulieren Sie den Auftrag selbst. Nennen Sie darin **keine** Konventionen und keine Marken, und verweisen Sie nicht auf `docs/konventionen.md`. Sie wollen sehen, was Ihre Instruktionen allein bewirken.

6. Prüfen Sie die Wirkung, bevor Sie die Änderungen übernehmen:

   - Lesen Sie den Diff (`git diff`, neue Dateien mit `git status`). Welche Marken stehen über welchen neuen Funktionen? Gehen Sie dann Ihre übrigen Regeln einzeln durch: eingehalten, verletzt oder im Diff nicht zu erkennen? Notieren Sie zu jeder Regel die Stelle.
   - Zeigt die Chat-Antwort an, welche Dateien Copilot als Kontext oder Referenz verwendet hat, sehen Sie dort nach, ob Ihre Instruktionsdateien dabei sind.
   - Lassen Sie `python -m pytest` laufen.
   - Rufen Sie den Bericht so auf, wie ein Kollege an der Theke es täte, und lesen Sie, was im Terminal steht:

     ```bash
     python -m scripts.bestandsbericht daten/bestand.csv --nachbestellliste /tmp/nachbestellung.csv
     ```

     Erfährt der Kollege, wie viele Artikel in der Liste stehen?

7. Übernehmen Sie das Ergebnis. Entfernen Sie vorher die Marken aus dem Code, sonst kann Copilot sie in späteren Läufen dort abschauen, und eine Marke beweist nichts mehr:

   ```bash
   sed -i '/^[[:space:]]*# Marke:/d' lager/*.py scripts/*.py tests/*.py
   grep -rn "Marke:" lager scripts tests
   ```

   `grep` soll nichts mehr finden. Findet es noch eine Marke am Ende einer Codezeile, löschen Sie den Kommentar von Hand. Dann:

   ```bash
   python -m pytest
   git add . && git commit -m "Nachbestellliste"
   ```

**Wenn Zeit bleibt, vor Schritt 7:**

- *Regel schärfen.* Hat eine Regel nicht gegriffen, suchen Sie die Ursache, bevor Sie die Regel umformulieren: Liegt die Datei am richtigen Ort, endet der Name richtig, passt das Muster auf die geänderte Datei? Dann schärfen Sie die Regel, verwerfen die Änderungen von Copilot (`git restore . && git clean -fd .`), committen die geschärfte Fassung und wiederholen den Auftrag in einem neuen Chat.
- *Gegenprobe ohne Instruktionen.* Legen Sie das Ergebnis des ersten Laufs beiseite und verschieben Sie `.github` aus dem Arbeitsbereich hinaus, damit der Agent den Ordner auch bei einer Suche nicht findet:

  ```bash
  git stash -u
  mv .github ../github_aus
  ```

  Stellen Sie denselben Auftrag in einem neuen Chat und vergleichen Sie den Diff mit Ihren Notizen zum ersten Lauf. Danach in genau dieser Reihenfolge zurück: erst den Ordner zurückholen, dann die Änderungen verwerfen, dann den ersten Lauf wiederherstellen:

  ```bash
  mv ../github_aus .github
  git restore . && git clean -fd .
  git stash pop
  git status
  ```

  `git status` zeigt jetzt wieder die Änderungen des ersten Laufs, `.github` ist unverändert. Weiter mit Schritt 7.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 1.

## Teil B: Ein Prompt File aufrufen

Neue Tests für eine Funktion entstehen im Team immer gleich: erst die Testfälle auflisten, dann die ausgewählten umsetzen. Das soll künftig ein Aufruf erledigen.

1. Legen Sie `.github/prompts/neuer-test.prompt.md` mit dem Gerüst unten an. Ersetzen Sie die beiden Stellen in spitzen Klammern. Für `agent` sind `ask`, `agent`, `plan` oder ein eigener Agent möglich.

   Wenn Sie schnell vorankommen, schreiben Sie das Prompt File ohne Gerüst selbst und vergleichen erst danach. Mögliche Felder im Frontmatter sind `description`, `name`, `argument-hint`, `agent`, `model` und `tools`. Variablen schreiben Sie als `${input:funktion}` oder mit Platzhalter `${input:funktion:Name der Funktion}`, Dateien binden Sie mit `#file:pfad` ein.

   ```markdown
   ---
   description: '<was dieses Prompt File tut, in einem Satz>'
   agent: '<Agent, der Dateien ändern darf>'
   ---
   Schreibe Tests für die Funktion `${input:funktion:Name der Funktion}`.

   1. Lies die Funktion und ihren Docstring. Nutze vorhandene Fixtures aus #file:tests/conftest.py.
   2. Liste zuerst die Testfälle auf, nummeriert: Normalfall, Grenzfälle, Fehlerfälle. Nenne zu jedem Fall Eingabe, erwartetes Ergebnis und woher die Erwartung stammt (Docstring oder Fachregel, nicht der aktuelle Code).
   3. Schreib noch keinen Code. Warte auf meine Auswahl der Nummern und setze dann nur diese Fälle um.
   4. Ändere keine bestehenden Tests. Lass am Ende `python -m pytest` laufen und zeig das Ergebnis.
   ```

2. Committen Sie das Prompt File:

   ```bash
   git add .github/prompts && git commit -m "Prompt File"
   ```

3. Rufen Sie es in einem neuen Chat mit `/neuer-test` auf, für `bestellmenge` oder `unter_mindestbestand`. Beobachten Sie, wie der Wert in die Variable kommt. Wählen Sie zwei oder drei der vorgeschlagenen Fälle aus.

4. Prüfen Sie den Diff wie in Teil A:

   - Welche Marken stehen über den neuen Tests? Das Prompt File erwähnt Ihre Instruktionen nicht.
   - Hat Copilot die Tests als Methoden der alten Klasse in `tests/test_auswertung.py` geschrieben oder als pytest-Funktionen, und in welche Datei? Was sagt die Team-Notiz dazu?

5. Entfernen Sie die Marken wie in Teil A, Schritt 7, lassen Sie die Tests laufen und committen Sie.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 2.

## Teil C: Wo wirkt Ihre Anpassung?

1. **Ihre Vorhersage**, bevor Sie etwas ausprobieren: Beantworten Sie jede Frage mit ja, nein oder weiß nicht und einem halben Satz Begründung. Schicken Sie die Antworten als kurze Nachricht in den Teams-Chat an den Trainer, etwa `1a nein, weil ...`. Schreiben Sie sie in keine Datei im Projekt.

   | Nr. | Situation | Frage |
   |---|---|---|
   | 1a | Sie tippen in VS Code in einer neuen Datei unter dem `applyTo`-Muster einer Ihrer pfadbezogenen Dateien, und Copilot macht einen Inline-Vorschlag (grauer Text). | Steht im Vorschlag `# Marke: repo`? |
   | 1b | wie 1a | Steht im Vorschlag die Marke dieser pfadbezogenen Datei? |
   | 2a | Der Agent im Chat ändert nur eine Datei, die **nicht** unter das Muster einer Ihrer pfadbezogenen Dateien fällt. | Steht `# Marke: repo` im Diff? |
   | 2b | wie 2a | Steht die Marke dieser pfadbezogenen Datei im Diff? |
   | 3a | Sie starten im Terminal im Ordner `starter` das Copilot CLI mit `copilot -sp "<Auftrag>"`. Der Auftrag verlangt eine neue Funktion für eine Datei unter dem Muster einer Ihrer pfadbezogenen Dateien. | Steht `# Marke: repo` in der Ausgabe? |
   | 3b | wie 3a | Steht die Marke dieser pfadbezogenen Datei in der Ausgabe? |
   | 3c | Derselbe Auftrag, gestartet an der Wurzel des Übungsrepos | Steht `# Marke: repo` in der Ausgabe? |
   | 4 | Sie starten im Ordner `starter` `copilot` interaktiv und rufen dort `/neuer-test` auf. | Läuft das Prompt File so wie im Chat von VS Code (Variable, Liste der Testfälle, Warten auf Ihre Auswahl)? |

2. **Prüfen.** Gehen Sie in dieser Reihenfolge vor:

   - **Situation 4 und 3 im Terminal.** Starten Sie im Ordner `starter` zuerst `copilot` interaktiv. Fragt das CLI, ob Sie dem Ordner vertrauen, bestätigen Sie. Rufen Sie `/neuer-test` auf. Sehen Sie danach mit `/instructions` nach, was das CLI Ihnen zeigt, und beenden Sie mit `/exit`. Dann Situation 3a und 3b:

     ```bash
     copilot -sp "Schreibe für eine neue Datei tests/test_grenzfall.py einen pytest-Test für bestellmenge aus lager/auswertung.py: ein Artikel, dessen Bestand genau dem Mindestbestand entspricht. Gib nur den Code aus und lege keine Datei an."
     ```

     Gilt keine Ihrer pfadbezogenen Dateien für `tests/`, verlangen Sie stattdessen eine Funktion für eine Datei unter Ihrem Muster, zum Beispiel: `"Schreibe für lager/auswertung.py eine Funktion gesamtbestellmenge, die die Bestellmengen aller Artikel unter Mindestbestand addiert. Gib nur den Code aus und lege keine Datei an."`

     Situation 3c, wenn Zeit bleibt: denselben Auftrag an der Wurzel des Übungsrepos, mit Pfad ab dort:

     ```bash
     cd "$(git rev-parse --show-toplevel)"
     copilot -sp "Schreibe für eine neue Datei 03_copilot_anpassen/starter/tests/test_grenzfall.py einen pytest-Test für bestellmenge aus 03_copilot_anpassen/starter/lager/auswertung.py: ein Artikel, dessen Bestand genau dem Mindestbestand entspricht. Lies nur diese eine Datei. Gib nur den Code aus und lege keine Datei an."
     cd -
     ```

   - **Situation 1 im Editor.** Schließen Sie alle Editor-Tabs, auch Ihre Instruktionsdateien: Ein Inline-Vorschlag kann Text aus geöffneten Dateien übernehmen. Legen Sie unter dem Muster einer pfadbezogenen Datei eine neue Datei an (bei einem Muster für Tests etwa `tests/test_probe.py`), tippen Sie eine Importzeile wie `from lager.auswertung import bestellmenge` und darunter zwei Leerzeilen. Warten Sie auf den grauen Vorschlag und lesen Sie ihn. Mit `Tab` übernehmen Sie ihn und sehen den nächsten. Löschen Sie die Datei danach wieder.

   - **Situation 2 im Chat, wenn Zeit bleibt.** Lassen Sie den Agenten in einem neuen Chat eine kleine Funktion in einer Datei ergänzen, die nicht unter das Muster einer Ihrer pfadbezogenen Dateien fällt, und sagen Sie dazu, dass er nur diese Datei ändert und keine Tests schreibt. Haben Sie eine pfadbezogene Datei für `tests/`, passt die Funktion `gesamtbestellmenge` in `lager/auswertung.py` von oben. Lesen Sie den Diff und verwerfen Sie die Änderung danach mit `git restore . && git clean -fd .`.

3. Schicken Sie zu jeder geprüften Frage in den Chat, was Sie gesehen haben, und ob die Beobachtung als Beleg reicht oder ob die Marke auch auf anderem Weg in das Ergebnis gekommen sein könnte. Die Auflösung aller Situationen kommt in der Nachbesprechung.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 3.

## Zusatzaufgabe (nach Teil C)

Das Team möchte einen Prüfer, der Dateien gegen die Konventionen liest und Befunde meldet, aber nie selbst etwas ändert.

1. Schreiben Sie einen Custom Agent `.github/agents/<name>.agent.md`. Frontmatter: `description` (Pflicht auf GitHub), `name` und `tools` mit einer Liste, die nur lesende Werkzeuge enthält. Welche Werkzeuge es gibt, zeigt Ihnen der Chat mit `/tools` oder in der Werkzeugauswahl. Ein Agent mit nur lesenden Werkzeugen kann Dateien lesen und durchsuchen, aber keine Befehle wie `git` ausführen. Schreiben Sie den Auftrag in der Agentendatei so, dass er mit genannten oder angehängten Dateien arbeitet.
2. Wählen Sie den Agenten im Chat aus. Hängen Sie `lager/export.py` und die Testdatei aus Teil A an (im Chat `#` tippen und die Datei wählen) und lassen Sie beide gegen die Konventionen prüfen.
3. Bitten Sie ihn danach ausdrücklich, den ersten Befund direkt in der Datei zu beheben. Prüfen Sie mit `git status`, ob sich eine Datei geändert hat.
4. Wenn Zeit bleibt: Rufen Sie denselben Agenten im CLI auf (`copilot --agent <name> -p "..."`), mit den Dateinamen im Auftrag. Verhält er sich gleich?

Ein Beispiel steht in `nach_dem_versuch.md`, Abschnitt 4.

## Zum Schluss: zurück zur Wurzel des Übungsrepos

Committen oder verwerfen Sie offene Änderungen, bis `git status` nichts mehr meldet. Öffnen Sie dann wieder das ganze Übungsrepo:

```bash
code -r "$(git rev-parse --show-toplevel)"
```

Das Fenster lädt neu, der Explorer zeigt wieder alle Übungen, und neue Terminals starten an der Wurzel des Übungsrepos. Dort beginnt Übung 4.
