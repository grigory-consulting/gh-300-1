# Übungen: GitHub Copilot

Vier Übungen zur Schulung GitHub Copilot (GH-300). Jede Übung ist ein kleines Python-Projekt mit Tests. Copilot schreibt den Code, Sie schreiben Anforderung und Prompt, prüfen Plan und Diff und entscheiden, was übernommen wird.

| Nr. | Übung | Dauer |
|---|---|---|
| 1 | [Anforderung und Plan](01_anforderung_und_plan/) | etwa 50 Minuten |
| 2 | [Tests und Fehlersuche](02_tests_und_fehlersuche/) | etwa 40 Minuten |
| 3 | [Copilot anpassen](03_copilot_anpassen/) | etwa 35 Minuten |
| 4 | [Ein Issue im Terminal bearbeiten](04_issue_im_terminal/) | etwa 25 Minuten |

## Folien

Die Folien zum Kurs liegen als PDF unter [folien/github-copilot-gh300.pdf](folien/github-copilot-gh300.pdf). GitHub zeigt sie direkt im Browser an; über **Download** speichern Sie sie lokal.

## Arbeitsumgebung: GitHub Codespace

Sie brauchen nur einen Browser und Ihren GitHub-Account mit Copilot-Plan. Python, pytest, die Erweiterung GitHub Copilot Chat und das Copilot CLI richtet der Codespace selbst ein.

1. Dieses Repository auf GitHub öffnen, **Code** > **Codespaces** > **Create codespace on main**. Der erste Start dauert einige Minuten.
2. In der Statusleiste unten das Copilot-Symbol prüfen: Es darf kein Hinweis auf eine fehlende Anmeldung erscheinen. Falls doch, über das Symbol anmelden.
3. Im Terminal (<kbd>Strg</kbd>+<kbd>ö</kbd> bzw. **Terminal** > **New Terminal**). Fragt VS Code vorher, ob Sie den Autoren der Dateien vertrauen, wählen Sie **Trust Folder & Continue**, sonst startet kein Terminal:

   ```bash
   python -m pytest --version
   copilot --version
   ```

4. Das Copilot CLI einmal starten (`copilot`) und mit `/exit` beenden. Im Codespace ist es bereits angemeldet; nur wenn es ausdrücklich nach einer Anmeldung fragt, geben Sie `/login` ein. In einem Unterordner fragt das CLI beim Start, ob Sie dem Ordner vertrauen. Warten Sie diese Frage ab, antworten Sie mit **1. Yes** und tippen Sie erst danach Ihren Auftrag, sonst gehen die ersten Zeichen verloren.
5. Unter dem Chat-Eingabefeld steht links, wo der Chat läuft. Stellen Sie dort **Local** ein. Ein neuer Chat über **+** startet oft wieder mit **Copilot**, und nur unter **Local** gibt es den Agenten **Plan**. Prüfen Sie die Einstellung deshalb bei jedem neuen Chat.

Zeigt `git diff` im Terminal am Ende einen Doppelpunkt, blättert Git gerade seitenweise. Mit **q** beenden Sie die Anzeige; `git --no-pager diff` gibt alles auf einmal aus.

Wer lieber mit dem lokalen VS Code arbeitet: Erweiterung **GitHub Codespaces** installieren und über die Befehlspalette **Codespaces: Connect to Codespace** wählen.

## So läuft jede Übung ab

1. README der Übung lesen und die Tests im `starter/`-Ordner einmal laufen lassen (`python -m pytest`).
2. Vorhersagen schicken Sie als kurze Nachricht im Teams-Chat an den Trainer, **bevor** Sie Copilot einsetzen. Schreiben Sie sie nicht in eine Datei im Repository: Copilot liest den Arbeitsbereich mit.
3. Anforderung und Prompt selbst formulieren. Der Prompt ist die eigentliche Übung, nicht der fertige Code.
4. Plan und Diff lesen, Tests laufen lassen, nachschärfen.
5. Beispiel-Prompts, Reflexionsfragen und Hinweise stehen in `nach_dem_versuch.md` im Ordner der Übung. Öffnen Sie dort nur den Abschnitt, auf den das README der Übung gerade verweist.

Eine Musterlösung besprechen wir gemeinsam nach jeder Übung.

## Nach dem Kurs

Codespaces verbrauchen Kontingent Ihres Accounts. Stoppen Sie den Codespace nach der Arbeit (**Code** > **Codespaces** > **…** > **Stop codespace**) und löschen Sie ihn, wenn Sie ihn nicht mehr brauchen.
