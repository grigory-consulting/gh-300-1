# Übung 1: Nach dem eigenen Versuch

Lesen Sie immer nur den Abschnitt, auf den das README gerade verweist. Die Abschnittsnummern entsprechen den Schritten im README.

Die Beispiel-Prompts sind eine mögliche Fassung. Vergleichen Sie: Was steht in Ihrem Prompt, das hier fehlt, und was steht hier, das in Ihrem fehlt?

`#anforderung.md` steht für die Referenz, die VS Code einfügt, wenn Sie `#` tippen und die Datei wählen. Die ältere Schreibweise `#file:anforderung.md` funktioniert weiter.

## Abschnitt 3: Beispiel-Prompt für den Plan

Agent: **Plan**

> Lies #anforderung.md, #betrag.py und #test_betrag.py.
> Erstelle einen Plan, wie `parse_betrag` die Anforderung erfüllt. Schreib noch keinen Code.
> Führe im Plan getrennt auf:
> 1. welche Eingaben du wie behandeln willst, jeweils mit Verweis auf das Akzeptanzkriterium,
> 2. jede Annahme, die nicht direkt aus der Anforderung folgt,
> 3. Fragen an mich, wo die Anforderung mehr als eine Lesart zulässt.

Zum Vergleich: Hat Ihr Prompt ausdrücklich nach Annahmen und nach offenen Fragen gefragt? Ohne diese Bitte müssen Sie die Annahmen selbst aus dem Plantext heraussuchen.

## Abschnitt 4: Beispiel-Prompt für die Umsetzung

Agent: **Agent**

> Setz den Plan um, mit dem aktuellen Stand von #anforderung.md.
> Randbedingungen:
> - Ändere nur `betrag.py` und `test_betrag.py`.
> - Keine neuen Abhängigkeiten, nur die Standardbibliothek.
> - Ändere keine vorhandenen Tests.
> - Schreib für jedes Akzeptanzkriterium einen Test, dessen Name das Kriterium erkennen lässt.
> - Führ danach `python -m pytest` im Ordner `starter` aus und zeig mir das Ergebnis.

Zum Vergleich: Welche dieser Randbedingungen stand in Ihrem Auftrag? Achten Sie in Schritt 5 besonders auf die, die fehlte.

## Abschnitt 6: Beispiel-Prompt für die Abschlussfrage

Selber Chat wie die Umsetzung:

> Welche Annahmen hast du getroffen, die nicht in der Anforderung standen? Nenn zu jeder die Stelle im Code und eine Eingabe, an der man sie sieht.

Mit der Eingabe je Annahme können Sie die Antwort sofort im Terminal prüfen.

## Abschnitt 8: Reflexion

- Legen Sie Ihre beiden Meldungen an den Trainer nebeneinander, aus Schritt 3 und aus Schritt 7: Minuten und `git diff --stat`. Was lesen Sie daraus?
- An welcher Stelle sind Ihnen Annahmen aufgefallen: im Plan, im Diff, bei der Abschlussfrage, beim Nachtrag? Gab es eine Stelle ohne jeden Fund?
- Welche Ihrer drei Antworten aus Schritt 2 haben gestimmt?
- Gab es Sätze in Ihrer Anforderung, die Copilot anders gelesen hat, als Sie sie gemeint haben? Welche?
- Was ist seit der ersten Fassung in `anforderung.md` dazugekommen, und woher kam jeweils der Anstoß (Fachbereich, Starter, Plan, Diff, Abschlussfrage, Nachtrag)?

  ```bash
  git diff anforderung-v1 -- anforderung.md
  ```

## Abschnitt 9: Zusatzaufgabe für nach dem Kurs

Die Firma hat eine Niederlassung in der Schweiz. Deren Belege sollen künftig über dieselbe Spesenabrechnung laufen. Die Beträge dort sind in Schweizer Franken und in Schweizer Schreibweise.

1. Fragen Sie Copilot (Agent: Ask oder Plan), was sich an Ihrer Anforderung ändert, wenn diese zweite Quelle dazukommt. Verlangen Sie ausdrücklich: zuerst die Änderungen an der Anforderung erklären, noch keinen Code.
2. Prüfen Sie die Erklärung: Stimmt, was Copilot über die Schweizer Schreibweise von Frankenbeträgen sagt? Was bedeutet die Änderung für Code, der die Funktion heute schon aufruft?
3. Übernehmen Sie, was Sie für richtig halten, in `anforderung.md`. Lassen Sie die Erweiterung dann wie in Schritt 4 und 5 umsetzen. Die bisherigen Tests müssen grün bleiben.
