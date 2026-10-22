# Übung 1: Anforderung und Plan

**Lernziel:** Sie schreiben eine Anforderung mit Akzeptanzkriterien, prüfen den Plan des Plan-Agenten gegen diese Anforderung und lassen erst danach den Agenten umsetzen. Sie schreiben Anforderung und Prompts, Copilot schreibt den Code, Sie prüfen Plan und Diff.

**Dauer:** etwa 50 Minuten

Beispiel-Prompts und Reflexion stehen in [nach_dem_versuch.md](nach_dem_versuch.md). Öffnen Sie dort immer nur den Abschnitt, auf den ein Schritt unten verweist.

## Ausgangslage

Ein kleines Team baut eine Spesenabrechnung. Die Beträge kommen aus drei Quellen. So sehen sie aus:

**Formular** (Feld "Betrag", so eingetippt):

```text
12,50
€ 8,90
12,-
```

**CSV-Export des Firmenkontos** (Kontoauszug):

```text
Buchungstag;Empfänger;Verwendungszweck;Betrag;Währung
02.10.2026;Hotel Adler;Rechnung 4471;-1.234,00;EUR
06.10.2026;Hotel Adler;Gutschrift 4471;150,00;EUR
```

**E-Mails** (Ausschnitte aus Rechnungen und Buchungsbestätigungen):

```text
Rechnungsbetrag: 89,90 €
Total: EUR 212.50
```

In [starter/betrag.py](starter/betrag.py) liegt eine erste Version von `parse_betrag(text: str) -> Decimal`. Sie liest die Beträge, die bisher im Formular vorkamen. Die Tests in [starter/test_betrag.py](starter/test_betrag.py) zeigen diese Fälle und laufen grün:

```bash
cd "$(git rev-parse --show-toplevel)/01_anforderung_und_plan/starter"
python -m pytest
```

Alle weiteren Befehle laufen in diesem Ordner.

Die Funktion soll künftig Beträge aus allen drei Quellen lesen. Was das genau heißt, legt Ihre Anforderung fest. Fachliche Rückfragen können Sie jederzeit an den Trainer stellen, er übernimmt die Rolle des Fachbereichs.

## Aufgabe

### 1. Anforderung schreiben

Legen Sie im Ordner `starter` die Datei `anforderung.md` an und schreiben Sie die Anforderung selbst, ohne Chat. Gliedern Sie sie so:

- **Ziel:** was die Funktion leistet und mit welcher Signatur.
- **Akzeptanzkriterien:** je Kriterium Given, When und Then, als eigene Zeile wie im Beispiel unten oder als Tabellenzeile.
- **Grenzfälle:** Eingaben, bei denen Sie selbst kurz überlegen mussten, und Ihre Entscheidung dazu.
- **Fehlerverhalten:** welche Eingaben abgelehnt werden und wie (welche Ausnahme, welche Meldung).
- **Nicht im Umfang:** was die Funktion ausdrücklich nicht leisten soll.

Ein Akzeptanzkriterium sieht zum Beispiel so aus:

```markdown
- Given die Eingabe "12,50", When parse_betrag aufgerufen wird, Then ist das Ergebnis Decimal("12.50").
```

Richtgröße: etwa 8 bis 12 Kriterien, Akzeptanz- und Fehlerfälle zusammen, in etwa 10 Minuten.

Prüfstein: Jemand anderes soll aus Ihrer Anforderung Tests ableiten können, ohne Sie zu fragen.

### 2. Vorhersage an den Trainer

Schicken Sie dem Trainer im Teams-Chat drei kurze Antworten. Schreiben Sie sie in keine Datei im Codespace.

1. Was liefert der heutige Starter für `"-1.234,00"`, für `"212.50"` und für `"12,-"`? Je ein Ergebnis oder der Name der Ausnahme.
2. Wie viele Rückfragen an Sie wird der erste Plan enthalten? Eine Zahl, auch 0 ist eine Antwort.
3. Bei welcher Eingabe aus Ihren Grenzfällen rechnen Sie am ehesten damit, dass der Plan nachfragt oder anders entscheidet als Sie? Eine Eingabe oder "keine".

Prüfen Sie danach Antwort 1 im Terminal:

```bash
python - <<'EOF'
from betrag import parse_betrag
for eingabe in ["-1.234,00", "212.50", "12,-"]:
    try:
        print(repr(eingabe), "->", repr(parse_betrag(eingabe)))
    except Exception as fehler:
        print(repr(eingabe), "->", type(fehler).__name__)
EOF
```

Wenn Sie das Ergebnis zu einer Änderung an `anforderung.md` bringt, nehmen Sie sie jetzt vor. Dann committen Sie den Stand und markieren die erste Fassung:

```bash
git add -A && git commit -m "Anforderung"
git tag anforderung-v1
```

Ab hier zeigt `git diff`, was sich seit diesem Stand geändert hat.

### 3. Plan erstellen lassen und prüfen

Merken Sie sich die Uhrzeit, wenn Sie den Auftrag an den Plan-Agenten abschicken.

1. Öffnen Sie einen neuen Chat, stellen Sie unter dem Eingabefeld **Local** ein und wählen Sie den Agenten **Plan**.
2. Formulieren Sie den Auftrag selbst. Geben Sie `anforderung.md`, `betrag.py` und `test_betrag.py` als Kontext mit: im Explorer Rechtsklick auf die Datei, dann **Add File to Chat**. Eine Datei, die im Editor offen ist, schlägt der Chat als gestrichelten Baustein vor; ein Klick auf **+** hängt sie fest an.
3. Lesen Sie den Plan Satz für Satz und halten Sie jede Aussage gegen Ihre Anforderung: Steht das so in `anforderung.md`, oder hat Copilot es angenommen?
4. Rückfragen stellt der Plan-Agent oft als kleines Formular mit Antwortvorschlägen. Halten Sie Ihre Antworten zusätzlich in `anforderung.md` fest, nicht nur im Chat. Den Chat sieht kein Kollege, die Datei liegt im Repository.
5. Hat sich die Anforderung geändert, lassen Sie den Plan neu erstellen und prüfen ihn noch einmal. Mehr als diese zweite Runde ist in der Zeit nicht vorgesehen.

Passt der Plan zu Ihrer Anforderung, schicken Sie dem Trainer im Teams-Chat zwei Angaben: die Minuten seit dem Abschicken des Auftrags und die letzte Zeile von `git diff --stat`.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 3.

### 4. Umsetzen lassen

Wählen Sie den Agenten **Agent** und schreiben Sie den Umsetzungsauftrag selbst. Begrenzen Sie ihn so, dass Sie den Diff danach in fünf Minuten prüfen können.

Unter dem fertigen Plan stehen Schaltflächen wie **Start Implementation** und **Start with Autopilot**. Nutzen Sie sie in dieser Übung nicht. Sie schickt womöglich einen fertigen Auftrag ab, in dem Ihre Begrenzung fehlt.

Wenn der Agent Befehle im Terminal ausführen will, lesen Sie den Befehl, bevor Sie ihn freigeben.

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 4.

### 5. Änderungen prüfen und Tests laufen lassen

Prüfen Sie die Änderungen, bevor Sie committen:

```bash
git status
git diff
```

`git status` zeigt auch neu angelegte Dateien, `git diff` zeigt nur Änderungen an Dateien, die Git schon kennt. Prüfen Sie:

- Wurden Dateien geändert oder angelegt, die nicht zu Ihrem Auftrag gehören?
- Hat jedes Akzeptanzkriterium einen Test? Prüft ein Test etwas, das nicht in der Anforderung steht?
- Verhält sich der Code bei Ihren Grenzfällen so, wie Sie es entschieden haben?

Dann:

```bash
python -m pytest
```

### 6. Abschlussfrage an Copilot

Fragen Sie im selben Chat, welche Annahmen Copilot getroffen hat, die nicht in der Anforderung standen. Formulieren Sie die Frage selbst.

Die Antwort ist eine neue Auskunft des Modells, kein Protokoll dessen, was der Code tut. Prüfen Sie jede genannte Annahme am Code oder mit einem Aufruf im Terminal wie in Schritt 2. Entscheiden Sie dann für jede:

- **übernehmen:** in `anforderung.md` eintragen,
- **ablehnen:** in `anforderung.md` eintragen, was stattdessen gelten soll.

Code und Tests passen Sie erst in Schritt 7 an. Committen Sie jetzt:

```bash
git add -A && git commit -m "Umsetzung"
```

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 6.

### 7. Nachtrag des Fachbereichs

Schreiben Sie dem Trainer im Teams-Chat "bereit für Schritt 7". Er schickt Ihnen einen Nachtrag des Fachbereichs.

Stellen Sie einen Timer auf 6 Minuten. Setzen Sie in dieser Zeit den Nachtrag und die in Schritt 6 eingetragenen Punkte um: `anforderung.md` anpassen, Auftrag an Copilot, Änderungen prüfen wie in Schritt 5, `python -m pytest`. Wenn der Timer abläuft, hören Sie auf, auch mitten im Schritt.

Schicken Sie dem Trainer dann wie in Schritt 3 die Minuten und die letzte Zeile von `git diff --stat`. Committen Sie den Stand, auch wenn er nicht fertig ist:

```bash
git add -A && git commit -m "Nachtrag"
```

### 8. Reflexion

Erst jetzt: `nach_dem_versuch.md`, Abschnitt 8. Beantworten Sie die Fragen für sich, das Gespräch folgt in der Nachbesprechung.

Abschnitt 9 enthält eine Zusatzaufgabe für die Zeit nach dem Kurs.
