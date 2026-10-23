# Übung 5 (Zusatz): Eine Agenten-Pipeline mit CrewAI bauen lassen

**Lernziel:** Sie lassen den Copilot-Agenten ein kleines Programm mit einer Bibliothek bauen, die sich schnell ändert, und prüfen das Ergebnis eines Sprachmodells gegen feste Sollwerte. Dabei gehen Sie mit einem API-Schlüssel so um, dass er nicht ins Repository gelangt.

**Dauer:** etwa 30 Minuten

## Ausgangslage

Die Fahrradwerkstatt aus Übung 3 bekommt ihre Eingangsrechnungen als PDF. Bisher tippt jemand Absender, Nummer, Datum und Beträge von Hand ab. Eine kleine Pipeline mit [CrewAI](https://docs.crewai.com/) soll das übernehmen: Ein erster Agent zieht die Felder aus dem Text der Rechnung, ein zweiter schreibt eine Kurzfassung für die Freigabe.

| Datei | Inhalt |
|---|---|
| `rechnungen/rechnung_1.pdf`, `rechnung_2.pdf` | zwei Eingangsrechnungen |
| `tests/test_ergebnisse.py` | prüft die Ergebnisse der Pipeline gegen die Werte auf den Rechnungen |
| `pruefe_zugang.py` | prüft, ob der Schlüssel funktioniert |
| `requirements.txt` | Abhängigkeiten mit festen Versionen |
| `.env.example` | Vorlage für den Schlüssel |

Copilot selbst kann CrewAI nicht als Sprachmodell dienen. Die Pipeline braucht deshalb einen eigenen Zugang zu einem Modell. Den Schlüssel dafür bekommen Sie vom Trainer.

## Vorbereitung

1. Terminal im Übungsordner öffnen und die Abhängigkeiten installieren. Das dauert ein bis zwei Minuten:

   ```bash
   cd "$(git rev-parse --show-toplevel)/05_crewai_pipeline/starter"
   pip install -r requirements.txt
   ```

2. Schlüssel eintragen. Kopieren Sie die Vorlage, öffnen Sie `.env` im Editor und ersetzen Sie `sk-...` durch den Schlüssel aus dem Teams-Chat:

   ```bash
   cp .env.example .env
   code .env
   ```

3. Zugang prüfen:

   ```bash
   python pruefe_zugang.py
   python -m pytest
   ```

   `pruefe_zugang.py` meldet „Zugang funktioniert“. Die Tests werden alle übersprungen, weil es noch keine Ergebnisse gibt.

4. Prüfen Sie, dass `.env` nicht im Repository landet:

   ```bash
   git status --short
   ```

   `.env` darf in der Liste nicht auftauchen.

## Aufgabe

1. Lesen Sie den Text der beiden Rechnungen, so wie die Pipeline ihn später bekommt, und dazu `tests/test_ergebnisse.py`:

   ```bash
   python -c "from pypdf import PdfReader; print(PdfReader('rechnungen/rechnung_2.pdf').pages[0].extract_text())"
   ```

   Schicken Sie dem Trainer im Teams-Chat Ihre Vorhersage: An welcher Stelle wird das Modell bei `rechnung_2.pdf` am ehesten einen falschen Wert liefern?

2. Schreiben Sie selbst den Auftrag an den Copilot-Agenten (neuer Chat, **Local**, **Agent**). Er soll eine Datei `pipeline.py` im Ordner `starter` anlegen. Was der Auftrag festlegen muss:

   - Aufruf `python pipeline.py rechnungen/rechnung_1.pdf`; das Ergebnis landet in `ergebnis/rechnung_1.json`, die Kurzfassung auf dem Bildschirm.
   - Den Text aus dem PDF liest `pypdf`. Kein Vektorindex, keine Embeddings.
   - Zwei Agenten mit CrewAI: Auslesen und Zusammenfassen.
   - Das Modell kommt aus `.env` (`LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`).
   - Die Felder der JSON-Datei, so wie die Tests sie lesen: `absender`, `rechnungsnummer`, `rechnungsdatum` (Format `JJJJ-MM-TT`), `betrag_netto`, `umsatzsteuer`, `betrag_brutto` und `positionen` mit `bezeichnung`, `menge`, `betrag`.
   - Die installierten Versionen aus `requirements.txt`. Neue Pakete nur nach Rückfrage.

3. Lesen Sie jede Werkzeuganfrage, bevor Sie sie freigeben. Will der Agent etwas installieren, das nicht in `requirements.txt` steht: ablehnen und nachfragen, wozu.

4. Pipeline für beide Rechnungen laufen lassen, dann testen:

   ```bash
   python pipeline.py rechnungen/rechnung_1.pdf
   python pipeline.py rechnungen/rechnung_2.pdf
   python -m pytest
   ```

5. Schlägt ein Test fehl: Finden Sie zuerst heraus, ob der Code falsch ist oder die Antwort des Modells. Öffnen Sie dazu die JSON-Datei und vergleichen Sie sie mit der Rechnung. Ändern Sie dann den Auftrag an das Modell in `pipeline.py`, nicht die Tests.

6. Die Tests prüfen nur die JSON-Datei, nicht die Kurzfassung. Lesen Sie die Kurzfassung zu `rechnung_2.pdf` Satz für Satz gegen den Text der Rechnung. Stimmt jede Aussage?

7. Lassen Sie jede Rechnung ein zweites Mal laufen. Sind die Ergebnisse gleich?

Erst jetzt: `nach_dem_versuch.md`.

## Wichtig zum Schlüssel

- `.env` steht in `.gitignore`. Committen Sie sie nie, auch nicht mit `git add -f`.
- Fügen Sie den Schlüssel nie in den Copilot-Chat ein und hängen Sie `.env` nicht als Kontext an.
- Der Trainer deaktiviert den Schlüssel nach dem Kurs. Für eigene Versuche danach brauchen Sie einen eigenen.
