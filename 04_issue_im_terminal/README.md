# Übung 4: Ein Issue im Terminal bearbeiten

**Lernziel:** Sie lassen Copilot CLI im Terminal ein Issue beheben, entscheiden jede Werkzeuganfrage selbst und prüfen das Ergebnis mit git. In einer zweiten Runde starten Sie das CLI mit einem Auftrag und Werkzeugfreigaben, die zur Aufgabe passen.

**Dauer:** etwa 25 Minuten

## Ausgangslage

Das Facility Management eines Bürogebäudes vergibt Besprechungsräume über ein Buchungsformular. Jede Nacht prüft das Paket `raumplan` die exportierten Buchungen auf Doppelbelegungen, am Morgen bekommt der Empfang den Bericht.

`raumplan` ist ein kleines Open-Source-Paket. Ihr Team pflegt es, auch andere Betreiber setzen es ein und melden Fehler im öffentlichen Ticketsystem des Projekts.

| Datei | Inhalt |
|---|---|
| `raumplan/buchung.py` | Buchungen aus der CSV-Datei lesen |
| `raumplan/konflikte.py` | Doppelbelegungen finden |
| `raumplan/__main__.py` | Aufruf `python -m raumplan pruefen DATEI.csv` |
| `scripts/nachtlauf.sh` | nächtliche Prüfung aller Dateien in `daten/` |
| `daten/buchungen_beispiel.csv` | Beispieldaten |
| `tests/` | pytest-Tests |
| `requirements.txt` | Abhängigkeiten |
| `issues/142.md` | Ticket #142, als Markdown aus dem Ticketsystem exportiert |

Ticket #142 ist Ihnen zugewiesen. Sie arbeiten in dieser Übung im Terminal.

## Vorbereitung

1. Haben Sie in Übung 3 den Ordner `starter` als Arbeitsbereich geöffnet, stellen Sie das Fenster zuerst wieder auf das ganze Übungsrepo: `code -r "$(git rev-parse --show-toplevel)"`. Öffnen Sie dann ein neues Terminal:

   ```bash
   cd "$(git rev-parse --show-toplevel)/04_issue_im_terminal/starter"
   git status
   ```

2. `git status` darf keine offenen Änderungen zeigen, auch nicht aus früheren Übungen, denn später setzen Sie das ganze Repo auf den Ausgangsstand zurück. Zeigt es Änderungen, committen Sie diese jetzt:

   ```bash
   git add -A
   git commit -m "Stand nach Übung 3"
   ```

3. Erst danach Tests und Hash des Ausgangsstands:

   ```bash
   python -m pytest
   git rev-parse --short HEAD
   ```

   Schicken Sie den Hash dem Trainer im Teams-Chat. Sie brauchen ihn zum Prüfen und Zurücksetzen.

Notizen machen Sie auf Papier oder im Teams-Chat, nicht in einer Datei im Repo.

## Runde 1: Issue beheben wie im Alltag

1. Schicken Sie dem Trainer, bevor Sie Copilot starten, Ihre Vorhersage als kurze Nachricht im Teams-Chat:

   - Welche Dateien wird der Agent ändern oder anlegen?
   - Welche Befehle wird er ausführen?
   - Wie viele Anfragen zum Schreiben oder Ausführen erwarten Sie?

2. Starten Sie das CLI im Ordner `starter`, ohne weitere Optionen:

   ```bash
   copilot
   ```

   Fragt das CLI, ob Sie den Dateien in diesem Ordner vertrauen, wählen Sie **Yes** (nur für diese Sitzung, nicht dauerhaft).

3. Geben Sie den Auftrag so ein, wie Sie ihn im Alltag formulieren würden, zum Beispiel:

   > Behebe das Issue in issues/142.md.

4. Das CLI fragt nach, bevor es eine Datei schreibt oder einen Befehl ausführt, der mehr tut als lesen. Entscheiden Sie jede Anfrage einzeln und so, wie Sie es im Alltag tun würden. Wählen Sie dabei immer die Option, die nur diese eine Aktion erlaubt, nicht die für die ganze Sitzung oder für das Repository. Notieren Sie jede Anfrage:

   | Nr. | Werkzeug (Datei schreiben, Shell-Befehl) | Datei oder Befehl | erlaubt / abgelehnt |
   |---|---|---|---|
   | 1 | | | |

5. Lesen Sie die Abschlussmeldung des Agenten. Fragen Sie in derselben Sitzung nach, bevor Sie sie beenden:

   > Welche Dateien hast du geändert oder angelegt, welche Befehle hast du ausgeführt? Welche Punkte aus issues/142.md hast du umgesetzt und welche nicht, jeweils mit Zeilennummer und Grund?

   Lesen Sie die Antwort und beenden Sie die Sitzung mit `/exit`.

## Prüfen: Was hat sich geändert?

Ersetzen Sie `<Hash>` durch den Hash aus der Vorbereitung:

```bash
git status
git log --oneline -3
git diff <Hash> --stat
git diff <Hash>
```

`git diff <Hash>` vergleicht den aktuellen Stand mit dem Ausgangsstand, auch wenn der Agent Dateien vorgemerkt (`git add`) oder committet hat. Neue Dateien, die git noch nicht kennt, stehen in `git status` unter "Untracked files"; lesen Sie sie mit `cat`.

Prüfen Sie:

- Welche Dateien hat der Agent geändert oder neu angelegt?
- Welche Befehle hat er ausgeführt (Ihre Liste aus Runde 1)? Welche davon sehen Sie im Diff nicht?
- Nennt die Abschlussmeldung alle Änderungen, die Sie im Diff sehen?
- Stimmt das Ergebnis? `python -m pytest` und der Befehl zum Nachstellen aus dem Issue.

Committen Sie diesen Stand nicht.

Erst jetzt: [nach_dem_versuch.md](nach_dem_versuch.md), Abschnitt 1. Dort geht es mit dem Prüfen weiter, danach folgen Runde 2 und die Reflexion.
