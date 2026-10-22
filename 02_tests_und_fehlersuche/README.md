# Übung 2: Tests und Fehlersuche

**Lernziel:** Fehler über Hypothesen eingrenzen, bevor Code geändert wird. Mit Copilot die Ursache roter Tests finden und beheben, Lücken in einer Testsuite finden und gezielt schließen.

**Dauer:** etwa 40 Minuten

## Ausgangslage

Ein Versandhändler zeigt im Warenkorb an, wann ein Paket beim Kunden ankommt. Das Paket `versand` im Ordner `starter/` berechnet aus dem Bestellzeitpunkt den Versandtag und den Zustelltermin. Die verbindlichen Regeln der Logistik stehen in [starter/docs/fachregeln.md](starter/docs/fachregeln.md).

| Datei | Inhalt |
|---|---|
| `versand/lieferdatum.py` | Versandtag und Zustelltermin |
| `versand/feiertage.py` | bundesweite Feiertage 2026 und 2027 |
| `versand/konfiguration.py` | Betriebsparameter |
| `tests/` | pytest-Tests |
| `docs/fachregeln.md` | Regeln der Logistik |

Dateien hängen Sie im Chat an, indem Sie `#` tippen und die Datei auswählen. VS Code fügt die Referenz in der aktuellen Form ein. Die ältere Schreibweise `#file:pfad` funktioniert weiter.

## Vorbereitung

Öffnen Sie im Codespace ein Terminal und wechseln Sie in den Übungsordner:

```bash
cd "$(git rev-parse --show-toplevel)/02_tests_und_fehlersuche/starter"
git status
```

## Teil A: Fehlersuche mit Hypothesen

1. Lassen Sie die Tests für die Lieferterminberechnung laufen:

   ```bash
   python -m pytest tests/test_lieferdatum.py
   ```

   Drei Tests schlagen fehl. Um diese drei geht es in Teil A.

2. Öffnen Sie den Chat und wählen Sie den Agenten **Ask**. Ask beantwortet Fragen und ändert keine Dateien.

3. Beginnen Sie mit `test_bestellung_ostermontag_vormittag`. Formulieren Sie dafür einen Debug-Prompt mit diesen sechs Teilen:
   1. **Problem:** welcher Test schlägt fehl
   2. **Erwartet:** was die Fachregeln verlangen
   3. **Tatsächlich:** was der Code liefert (aus der Testausgabe)
   4. **Reproduktion:** der Befehl, der genau diesen Test startet (`-k <testname>`)
   5. **Relevanter Code:** die Datei mit der Funktion, die der Test aufruft; die Testausgabe als Text eingefügt oder über `#execute/testFailure` (alte Form `#testFailure`), wenn Sie die Tests in der Ansicht **Testing** ausgeführt haben
   6. **Bisher geprüft:** was Sie selbst schon ausgeschlossen haben

4. Bitten Sie Copilot um Hypothesen, geordnet nach Wahrscheinlichkeit, zu jeder Hypothese genau eine Prüfung, die sie widerlegen würde. Verlangen Sie ausdrücklich noch keinen Fix.

5. Führen Sie die Prüfungen selbst aus, zum Beispiel im Terminal mit `python -c "..."` oder mit einem einzelnen Test. Glauben Sie einer Hypothese erst, wenn sie ihre Prüfung überstanden hat.

6. Erst mit bestätigter Hypothese wechseln Sie zum Agenten **Agent** und verlangen einen minimalen Fix für genau diese Ursache. Lesen Sie den Diff, bevor Sie ihn annehmen.

7. Die beiden übrigen Fehlschläge brauchen keine Hypothesenrunde. Vergleichen Sie die erwarteten Termine mit dem Kalender und mit Abschnitt 1 der Fachregeln, benennen Sie die Ursache in einem Satz und lassen Sie im Agenten **Agent** genau diese Ursache beheben. Auch hier lesen Sie den Diff, bevor Sie ihn annehmen.

8. Lassen Sie die Tests erneut laufen, bis `tests/test_lieferdatum.py` grün ist.

9. Committen Sie Ihre Korrekturen:

   ```bash
   git add . && git commit -m "<Ihre Nachricht>"
   ```

Erst jetzt: Vergleichen Sie Ihre Prompts mit `nach_dem_versuch.md`, Abschnitt 1.

## Teil B: Den Agenten selbständig arbeiten lassen

In Teil A haben Sie jeden Schritt selbst geführt. Jetzt geben Sie dem Agenten einen kurzen Auftrag und lassen ihn Tests ausführen, ändern und nachprüfen, wie im Arbeitsalltag.

1. Lassen Sie die gesamte Testsuite laufen:

   ```bash
   python -m pytest
   ```

2. Öffnen Sie einen **neuen Chat** und wählen Sie den Agenten **Agent**.

3. Formulieren Sie in ein bis zwei Sätzen den Auftrag, die restlichen Fehlschläge zu beheben. Der Agent darf die Tests selbst ausführen und so lange nachbessern, bis die Suite grün ist.

4. Bestätigen Sie Terminalbefehle, wenn der Agent danach fragt. Lesen Sie den Diff, bevor Sie ihn annehmen.

5. Lassen Sie die Suite selbst noch einmal laufen und committen Sie:

   ```bash
   python -m pytest
   git add . && git commit -m "<Ihre Nachricht>"
   ```

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 2.

## Teil C: Lücken in den Tests

1. **Ihre Vorhersage:** Suchen Sie in den Fachregeln zwei Fälle, die Ihrer Meinung nach in den vorhandenen Tests fehlen. Schicken Sie beide Fälle im Teams-Chat an den Trainer, zu jedem Fall ein Ja oder Nein: Nennt Copilot ihn in seiner Liste?

2. Fragen Sie im Agenten **Ask** nach fehlenden Testfällen. Hängen Sie Code, Tests und Fachregeln an. Verlangen Sie eine Liste mit Begründung und noch keine Tests.

3. Vergleichen Sie die Liste mit Ihrer Vorhersage und mit den Fachregeln. Streichen Sie, was fachlich keine Rolle spielt. Wählen Sie zwei bis drei Grenzfälle aus.

4. Lassen Sie genau diese Fälle als Tests in einer neuen Datei `tests/test_grenzfaelle.py` umsetzen, im Agenten **Agent** oder mit `/tests` auf der markierten Funktion. Prüfen Sie jeden erwarteten Wert selbst an Kalender und Fachregeln, bevor Sie ihn übernehmen.

5. Lassen Sie alle Tests laufen. Schlägt ein neuer Test fehl, gehen Sie vor wie in Teil A.

6. Committen Sie.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 3, danach die Reflexion in Abschnitt 4.
